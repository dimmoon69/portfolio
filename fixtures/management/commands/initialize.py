from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser({
            "username": "app",
            "email": "super@user.me",
            "password": "***super@user***"
        })
