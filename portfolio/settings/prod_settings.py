import os
from .base_settings import BASE_DIR

DEBUG = False

SECRET_KEY = ")gj8u2&jmv(zt%n=z7r&z-y(l!q2(zlvv=_d0j7qheacql7)d^"

ALLOWED_HOSTS = [
    "*",
]

EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "info@myskill.site"
EMAIL_HOST_PASSWORD = "Dima"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "myskill",
        "USER": "myskill_user",
        "PASSWORD": "myskillPSWD8594",
        "HOST": "myskill-postgres",
        "PORT": 5432,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
