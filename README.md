# Explore Russia <br /><br />

## Установка проекта и зависимостей <br /><br />

### Установка проекта
```git clone https://github.com/ZenoFromoren/explore-russia-backend-django.git``` <br /><br />

### Установка зависимостей
В папке с установленным проектом
```python -m venv venv```

```venv/Scripts/activate```

```pip install -r requirements.txt``` <br /><br />

### Запуск проекта
```cd explore-russia-backend-django``` (из корневой папки)
```python manage.py runserver``` <br /><br />

## Информация о проекте
Стек: Django, DRF, PostgreSQL, DRF-nested-routes, Docker, Nginx <br /><br />

### Основные сущности <br /><br />

#### Пользователи (users)
Содержит
- Имя (username)
- Пароль (password)
- E-mail
- Город (city)
- Информацию о себе (about)
- Аватар (avatar)
- Дату регистрации (date_joined)

Авторизация пользователей выполняена с помощью JWT <br /><br />

#### Посты (posts)
Содержит
- Город (city)
- Заголовок (title)
- Текст (text)
- Превью картинку (image)
- Дату создания (created_at)
- Дату изменение (updated_at) <br /><br />

#### Комментарии (comments)
Содержит
- Текст (text)
- Дату создания (created_at)
- Дату изменение (updated_at)
- Родительский комментарий (parent)
- Пост (post)
- Автора (owner)
- Поле, обозначающее, был ли комментарий отредактирован (is_edited) <br /><br />
