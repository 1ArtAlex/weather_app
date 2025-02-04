
# Weather App

## Описание
Это веб-приложение позволяет пользователям вводить название города и получать прогноз погоды для этого города. Приложение использует API погоды и сохраняет историю поиска для каждого пользователя.

## Использованные технологии
- Flask.
- SQLAlchemy.
- Docker.

## Функционал
- Ввод города и получение прогноза погоды.
- Сохранение истории поиска.
- Автодополнение (подсказки) при вводе города.
- API для отображения истории поиска.

## Структура проекта
```
weather_app/
│
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py/
│
├── tests/
│   └── test_routes.py
│
├── app.db
├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md
```

- **app/**: Каталог приложения Flask.
  - **__init__.py**: Инициализация приложения Flask.
  - **forms.py**: Определение WTForms для веб-форм.
  - **models.py**: Определение моделей базы данных SQLAlchemy.
  - **routes.py**: Определение маршрутов и контроллеров Flask.
  - **templates/**: HTML-шаблоны для отображения страниц.
    - **index.html**: Шаблон для главной страницы с формой ввода города.
- **tests/**: Каталог с тестами.
  - **test_routes.py**: Тесты для проверки маршрутов и контроллеров.
- **Dockerfile**: Файл для создания Docker-образа приложения.
- **docker-compose.yml**: Файл для настройки и запуска Docker-контейнеров.
- **requirements.txt**: Список Python библиотек и их версий для установки.
- **run.py**: Входная точка для запуска приложения.


## Запуск
1. Склонируйте репозиторий:
    ```sh
    git clone https://github.com/1ArtAlex/weather_app.git
    cd weather_app
    ```
2. Запуск:
    ```sh
    docker-compose up --build
    ```
    
    (при запуске через докер может не работать автодополненин, так как города берутся из удаленного подключения к бд, а через докер к ней (пока) подключение не настроено)

    или

    ```sh
    flask run
    ```
3. Приложение будет доступно по адресу `http://localhost:5000`.

## Тестирование
Для запуска тестов (тесты проходят пока не все, разбираюсь в чем проблема):
```sh
pytest
```
