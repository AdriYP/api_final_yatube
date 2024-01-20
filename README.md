# API для Yatube
**Yatube** — это платформа для блогов, и представляет блог-сервис для пользователей с возможностью
зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора.\
В проекте реализовано бэкенд приложение для работы с API, базирующееся на фреймворке Django REST Framework (DRF), предоставляющее функционал CRUD операций при работе с учётными записями, постами, комментариями и группами.\
Данный проект является учебным и разработан в рамках обучения на курсе Python-разработчик плюс от Яндекс Практикум учащимся Мироновым Владимиром Анатолиевичем.

## Установка проекта
1. Клонирование репозитория:

`git@github.com:AdriYP/api_final_yatube.git`

2. Переход в директорию yatube_api:

`cd api_final_yatube`

3. Создание виртуального окружения:

`python -m venv venv`

4. Активация виртуального окружения:

`source venv/Scripts/activate`

5. Установка и обновление менеджера пакетов PIP:

`python -m pip install --upgrade`

6. Установка зависимостей:

`pip install -r requirements.txt`

7. Выполнение миграций:

`python manage.py migrate`

8. Запуск сервера:

`python manage.py runserver`

## Эндпоинты API
Список эндпоинтов проекта доступен в документации по ссылке 'http://127.0.0.1:8000/redoc/'

## Примеры запросов

### Создание поста (POST запрос)
Эндпоинт `../api/v1/posts/`
```json
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Ответ на запрос:
```json
{    
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
### Получение комментария к посту (GET запрос)
Эндпоинт `../api/v1/posts/{post_id}/comments/{id}/`
```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
### Получение списка сообществ (GET запрос)
Эндпоинт `../api/v1/groups/`
```json
[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]
```