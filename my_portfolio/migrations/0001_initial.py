# Generated by Django 3.0.3 on 2020-11-21 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категории')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_small', models.ImageField(upload_to='photo_user', verbose_name='Фото')),
                ('photo_big', models.ImageField(upload_to='photo_user', verbose_name='Фото 5760x3048')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('telegram', models.CharField(max_length=15, verbose_name='Телеграм')),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='Телефон')),
                ('skype', models.CharField(max_length=15, verbose_name='Скайп')),
                ('hello', models.TextField(verbose_name='Приветствие')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиль',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Используемые технологии',
                'verbose_name_plural': 'Используемые технологии',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('url', models.SlugField(max_length=250, unique=True)),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('dns', models.CharField(max_length=250, verbose_name='Доменное имя')),
                ('link', models.URLField(verbose_name='Ссылка на сайт')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('draft', models.BooleanField(default=False, verbose_name='Модерация')),
                ('photo', models.ImageField(upload_to='my_work', verbose_name='Фото')),
                ('tags', models.ManyToManyField(to='my_portfolio.Tag', verbose_name='Используемые технологии')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Соцсеть')),
                ('icon', models.CharField(max_length=100, verbose_name='Иконка соцсети')),
                ('link', models.URLField(verbose_name='Ссылка на сайт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_network', to='my_portfolio.Profile', verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Соцсеть',
                'verbose_name_plural': 'Соцсети',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Навык')),
                ('percent', models.PositiveIntegerField(verbose_name='Процент')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='my_portfolio.Profile', verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('text', models.TextField(max_length=500, verbose_name='Отзыв')),
                ('sequence', models.PositiveIntegerField(verbose_name='Очередность')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='my_portfolio.Work', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок статьи')),
                ('url', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('text_min', models.TextField(max_length=120, verbose_name='Текст мин.')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации статьи')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи')),
                ('date_edit', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования статьи')),
                ('draft', models.BooleanField(default=False, verbose_name='Модерация')),
                ('image', models.ImageField(upload_to='article', verbose_name='Изображение')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_portfolio.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статью',
                'verbose_name_plural': 'Статьи',
                'ordering': ('-date_publication',),
            },
        ),
    ]