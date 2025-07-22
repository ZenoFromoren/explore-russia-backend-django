# Explore Russia



## Установка проекта и зависимостей



### Установка проекта 
```git clone https://github.com/ZenoFromoren/explore-russia-backend-django.git```



### Установка зависимостей
В папке с установленным проектом
```python -m venv venv```

```venv/Scripts/activate```

```pip install -r requirements.txt```



### Запуск проекта
```cd explore-russia-backend-django``` (из корневой папки)
```python manage.py runserver```



## Информация о проекте
Стек: Django, DRF, PostgreSQL, DRF-nested-routes, Docker, Nginx



### Основные сущности



#### Пользователи (users)
Содержит
- Имя (username)
- Пароль (password)
- E-mail
- Город (city)
- Информацию о себе (about)
- Аватар (avatar)
- Дату регистрации (date_joined)

Авторизация пользователей выполняена с помощью JWT



#### Посты (posts)
Содержит
- Город (city)
- Заголовок (title)
- Текст (text)
- Превью картинку (image)
- Дату создания (created_at)
- Дату изменение (updated_at)



#### Комментарии (comments)
Содержит
- Текст (text)
- Дату создания (created_at)
- Дату изменение (updated_at)
- Родительский комментарий (parent)
- Пост (post)
- Автора (owner)
- Поле, обозначающее, был ли комментарий отредактирован (is_edited) 
