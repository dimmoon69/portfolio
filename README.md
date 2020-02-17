Portfolio
=========
Portfolio - это веб-базированный ресурс, который отражает рост учебных или профессиональных достижений владельца.
Веб-портфолио школьника и студента — это веб-сайт, на котором отражаются образовательные результаты — результаты
выполнения лабораторных работ, проектных заданий.

- Python 3.6
- Django 3

Установка
---------
1 Создайте виртуальное окружение.

    python -m venv venv

2 Активируйте витуальное окружение.

    source venv/bin/activate

3 Установите зависимости:

    pip install -r requirements.txt
    
    python manage.py makemigrations
    
    python manage.py migrate
    
4 Создайте суперпользователя

    python manage.py createsuperuser

Настройка
---------
Создайте файл secret_key.py и добавьте в него следующие настройки:

    SECRET_KEY = 'Секретный ключ проекта'

    EMAIL_HOST_USER = 'Название почтового ящика'

    EMAIL_HOST_PASSWORD = 'Пароль от почтового ящика'

Запуск
------
В активированном виртуальном окружении выполните:

    python manage.py runserver