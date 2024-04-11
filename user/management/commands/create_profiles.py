from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from user.models import UserProfile

class Command(BaseCommand):
    help = 'Creates profiles for existing users'

    def handle(self, *args, **options):
        existing_users = User.objects.all()
        for user in existing_users:
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user)