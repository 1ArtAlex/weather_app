
# Weather App

## Описание
Это веб-приложение позволяет пользователям вводить название города и получать прогноз погоды для этого города. Приложение использует API погоды и сохраняет историю поиска для каждого пользователя.

## Установленные технологии
- Flask: Фреймворк для создания веб-приложений на языке Python.
- SQLAlchemy: ORM (Object-Relational Mapping) для работы с базой данных.
- Docker: Платформа для разработки, доставки и запуска приложений в контейнерах.

## Функционал
- Ввод города и получение прогноза погоды.
- Сохранение истории поиска.
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

## Запуск
1. Склонируйте репозиторий:
    ```sh
    git clone https://github.com/1ArtAlex/weather_app.git
    cd weather_app
    ```
2. Запустите Docker:
    ```sh
    docker-compose up --build
    ```
3. Приложение будет доступно по адресу `http://localhost:5000`.

## Тестирование
Для запуска тестов:
```sh
pytest
```