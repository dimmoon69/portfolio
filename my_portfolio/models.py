from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Profile(models.Model):
    """Профиль пользователя"""

    user = models.OneToOneField(User, verbose_name="Имя пользователя", on_delete=models.CASCADE)
    photo_small = models.ImageField("Фото", upload_to="photo_user")
    photo_big = models.ImageField("Фото 5760x3048", upload_to="photo_user")
    position = models.CharField("Должность", max_length=100)
    birthday = models.DateField("День рождения")
    address = models.CharField("Адрес", max_length=100)
    telegram = models.CharField("Телеграм", max_length=15)
    phone = models.CharField("Телефон", max_length=25, blank=True)
    skype = models.CharField("Скайп", max_length=15)
    hello = models.TextField("Приветствие")

    def __str__(self):
        return f"Пользователь {self.user.first_name}"

    def age(self):
        import datetime
        td = datetime.datetime.now().date()
        age_years = int((td - self.birthday).days / 365)
        return age_years

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"


class SocialNetwork(models.Model):
    """Соцсети"""
    user = models.ForeignKey(Profile, verbose_name="Имя пользователя", on_delete=models.CASCADE, related_name="social_network")
    name = models.CharField("Соцсеть", max_length=100)
    icon = models.CharField("Иконка соцсети", max_length=100)
    link = models.URLField("Ссылка на сайт")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Соцсеть"
        verbose_name_plural = "Соцсети"


class Skill(models.Model):
    """Навыки"""
    user = models.ForeignKey(Profile, verbose_name="Имя пользователя", on_delete=models.CASCADE, related_name="skill")
    name = models.CharField("Навык", max_length=100)
    percent = models.PositiveIntegerField("Процент")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class Tag(models.Model):
    """Теги"""
    # work = models.ForeignKey(Work, verbose_name="Проект", on_delete=models.CASCADE, related_name="tags")
    name = models.CharField("Тег", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Используемые технологии"
        verbose_name_plural = "Используемые технологии"


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категории", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Work(models.Model):
    """Проекты"""

    title = models.CharField("Заголовок", max_length=250)
    url = models.SlugField(max_length=250, unique=True)
    text = models.TextField("Текст статьи")
    dns = models.CharField("Доменное имя", max_length=250)
    link = models.URLField("Ссылка на сайт")
    tags = models.ManyToManyField(Tag, verbose_name="Используемые технологии")
    publish = models.DateTimeField("Дата публикации", default=timezone.now)
    draft = models.BooleanField("Модерация", default=False)
    photo = models.ImageField("Фото", upload_to="my_work")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.photo.path)

        if image.height > 740 or image.width > 740:
            resize = (740, 740)
            image.thumbnail(resize)
            image.save(self.photo.path)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ("-publish",)


class Recommendation(models.Model):
    """Отзывы"""
    work = models.ForeignKey(Work, verbose_name="Проект", on_delete=models.CASCADE, related_name="recommendations")
    name = models.CharField("ФИО", max_length=100)
    text = models.TextField("Отзыв", max_length=500)
    sequence = models.PositiveIntegerField("Очередность")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Article(models.Model):
    """Статья"""

    title = models.CharField("Заголовок статьи", max_length=250)
    url = models.SlugField("URL", max_length=250, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    text_min = models.TextField("Текст мин.", max_length=120)
    text = models.TextField("Текст статьи")
    date_publication = models.DateTimeField("Дата публикации статьи", default=timezone.now)
    date_creation = models.DateTimeField("Дата создания статьи", auto_now_add=True)
    date_edit = models.DateTimeField("Дата редактирования статьи", auto_now=True)
    draft = models.BooleanField("Модерация", default=False)
    image = models.ImageField("Изображение", upload_to="article")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.image.path)

        if image.height > 720 or image.width > 940:
            resize = (720, 940)
            image.thumbnail(resize)
            image.save(self.image.path)

    def get_absolute_url(self):
        return reverse("blog", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"
        ordering = ("-date_publication",)