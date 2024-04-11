from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    date_of_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=150, blank=True)
    additional_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

