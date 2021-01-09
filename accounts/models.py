from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomAccount(AbstractUser):
    email = models.EmailField('Endereço de email', unique=True)

class Profile(models.Model):
    account = models.ForeignKey(CustomAccount, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{ self.account.username } - { self.name }'