Portfolio
=========
Portfolio - это веб-базированный ресурс, который отражает рост учебных или профессиональных достижений владельца.
Веб-портфолио школьника и студента — это веб-сайт, на котором отражаются образовательные результаты — результаты
выполнения лабораторных работ, проектных заданий.

- Python 3.6
- Django 3

Установка и Настройка
---------------------
Создайте папку проекта, где будет храниться проект.

1 Скопируйте проект из GitHub в новь созданную директорию.

    git clone https://github.com/dimmoon69/portfolio.git
    
2 Создайте файл local_settings.py и добавьте в него следующие настройки.

    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = 'Секретный ключ проекта'

    DEBUG = True

    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [STATIC_DIR]

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'Название почтового ящика@gmail.com'
    EMAIL_HOST_PASSWORD = 'Пароль от почтового ящика'
    
3 Создайте виртуальное окружение.

    python -m venv venv

4 Активируйте витуальное окружение.

    source venv/bin/activate

5 Установите зависимости.

    pip install -r requirements.txt
    
6 Создайте файл миграций.
    
    python manage.py makemigrations
    
7 Создайте таблицы в базе данных.   
    
    python manage.py migrate
    
8 Создайте суперпользователя.

    python manage.py createsuperuser

Запуск
------
В активированном виртуальном окружении выполните.

    python manage.py runserver
