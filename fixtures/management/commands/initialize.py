from django.contrib.auth.models import User
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create_superuser({
                "username": "super_user",
                "email": "super@user.me",
                "password": "***super@user***"
            })
        except Exception as e:
            pass
