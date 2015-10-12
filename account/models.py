from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=128)
    class Admin:
        list_display = ('user', 'phone')


