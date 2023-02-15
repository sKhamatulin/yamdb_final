# API for "Yambd"
http://158.160.8.22/admin/

![yamdb_workflow](https://github.com/sKhamatulin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)



- Yambd - ресурс для отзывов на книги, фильмы, музыку.
___

## Установка на локальной машине.

### Cистемные требования:
    python==3
    Django==2.2
    DjangoRestFramework==3.12
    JWT

### Порядок установки.
1) Клонировать
2) Установить зависимости
3) Запустить

```
git clone github.com/sKhamatulin/api_yamb_final
pip install -r requirements.txt
python manage.py runserver
```

Проект запускается сервере разработчика на порте 8000(default).

```
Права доступа: Доступно без токена.
GET /api/v1/categories/ - Получение списка всех категорий
GET /api/v1/genres/ - Получение списка всех жанров
GET /api/v1/titles/ - Получение списка всех произведений
GET /api/v1/titles/{title_id}/reviews/ - Получение списка всех отзывов
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Получение списка всех комментариев к отзыву
Права доступа: Администратор
GET /api/v1/users/ - Получение списка всех пользователей
```

### Пользовательские роли

- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (user) — Аноним + право публиковать отзывы и ставить оценку произведениям,  комментировать чужие отзывы; редактировать и удалять свои отзывы и комментарии. default для новых зарегистрировавшихся
- Модератор (moderator) — user + право удалять любые отзывы и комментарии.
- Администратор (admin) — полные права + может назначать роли пользователям.
- Суперюзер Django (superusr) = (admin)


## Установка на докера.

*из директории `infra/`*
```
docker-compose up -d --build
```
Выполнить миграции:
```
docker-compose exec web python manage.py migrate
```
Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
Собрать статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```

## Для проекта написан скрипт yamdb_workflow.yml

скрипт запускает последовательно 

- тесты
- сбор и размещение контейнера на dockerHub
- деплой проекта на боевой сервер (ВМ на Яндекс.Облако)
- отправка сообщения в телеграм бот после успешного деплоя.


## Проект использует PostgreSQL, gunicorn, nginx
