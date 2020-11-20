from datetime import datetime

from django.core.mail import send_mass_mail
from django.views.generic import CreateView

from portfolio.settings import EMAIL_HOST_USER
from .models import Message


class MessageView(CreateView):
    """Сообщение"""

    model = Message
    fields = ["name", "email", "text"]
    success_url = "/"

    def form_valid(self, form):
        now = datetime.now()
        name = self.request.POST["name"]
        text = self.request.POST["text"]
        email = self.request.POST["email"]
        message = (
            "Новое сообщение.",
            "{}\n\n{}\nemail: {}".format(text, name, email),
            EMAIL_HOST_USER,
            [EMAIL_HOST_USER],
        )
        message_to_client = (
            "Ваше сообщение было получено {}.".format(now.strftime("%d-%m-%Y %H:%M")),
            "Текст Вашего сообщения:\n\n{}\n\n{}\nemail: {}".format(text, name, email),
            EMAIL_HOST_USER,
            [email],
        )
        send = send_mass_mail((message, message_to_client), fail_silently=False)
        return super().form_valid(form)
