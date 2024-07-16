# api_final
### Описание:

API проект служит для создании и получения информаии о постах, комментариях и подписках пользователей

### Установк:

Клонировать репозиторий и перейти в него в командной строке

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

### Примеры:

Запросы по постам. Доступны GET, POST, GET по конкретному посту, PUT, PATCH, DELETE

http://127.0.0.1:8000/api/v1/posts/

Доступно: limit - Количество публикаций на страницу, offset - Номер страницы после которой начинать выдачу

Запросы по комментариям. Доступны GET, POST, GET по конкретному комментарию, PUT, PATCH, DELETE

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Запросы по сообществам. Доступны GET и GET по конкретному сообществу

http://127.0.0.1:8000/api/v1/groups/

Запросы по подпискам. Доступны GET и POST

http://127.0.0.1:8000/api/v1/follow/

Возможен поиск по подпискам по параметру search

Работы с JWT-токеном

Получить: http://127.0.0.1:8000/api/v1/jwt/create/

Обновить: http://127.0.0.1:8000/api/v1/jwt/refresh/

Проверить: http://127.0.0.1:8000/api/v1/jwt/verify/
