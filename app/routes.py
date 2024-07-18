from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import CityForm
from app.models import CitySearch
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
import requests


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CityForm()
    weather = None

    if form.validate_on_submit():
        city = form.city.data
        weather = get_weather(city)

        if weather:
            flash(f'Weather in {city}: {weather}')

            city_search = CitySearch.query.filter_by(city_name=city).first()
            if city_search:
                db.session.delete(city_search)
                db.session.commit()
            city_search = CitySearch(city_name=city)
            db.session.add(city_search)
            db.session.commit()

    search_history = [entry.city_name for entry in CitySearch.query.order_by(CitySearch.id.desc()).limit(3).all()]

    return render_template('index.html', form=form, weather=weather, search_history=search_history)


@app.route('/api/cities', methods=['GET'])
def cities():
    q = request.args.get('q')
    if not q:
        return jsonify([])
    geolocator = Nominatim(user_agent="weather_app")
    locations = geolocator.geocode(q, exactly_one=False)
    cities = [{'name': location.address} for location in locations] if locations else []
    return jsonify(cities)


def get_coordinates(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None, None


def get_weather(city):
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return None

    api_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        weather_data = data['current_weather']

        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lat=lat, lng=lon)
        if timezone_str:
            local_timezone = pytz.timezone(timezone_str)
        else:
            local_timezone = pytz.utc

        utc_time = datetime.strptime(weather_data['time'], '%Y-%m-%dT%H:%M')
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)

        weather_data['time'] = local_time.strftime('%Y-%m-%d')

        return weather_data

    return None


@app.route('/api/history', methods=['GET'])
def history():
    history = CitySearch.query.order_by(CitySearch.id.desc()).limit(3).all()
    cities = [{'city': h.city_name} for h in history]
    return jsonify(cities)
