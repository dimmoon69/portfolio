DEBUG = False

SECRET_KEY = ')gj8u2&jmv(zt%n=z7r&z-y(l!q2(zlvv=_d0j7qheacql7)d^'
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myskill',
        'USER': 'myskill_user',
        'PASSWORD': 'myskillPSWD8594',
        'HOST': 'myskill-postgres',
        'PORT': 5432
    }
}
