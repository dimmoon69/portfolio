from django.db import models


class Message(models.Model):
    """Сообщение"""

    name = models.CharField("Имя", max_length=100)
    email = models.EmailField()
    text = models.TextField("Сообщение", max_length=5000)
    date = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
