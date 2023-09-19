from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

