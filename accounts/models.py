from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Movie

class CustomAccount(AbstractUser):
    email = models.EmailField('Endereço de email', unique=True)

class Profile(models.Model):
    main_profile = models.BooleanField(default=False)
    account = models.ForeignKey(CustomAccount, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=100)
    watch_list = models.ManyToManyField(Movie, related_name='profile_watch_list', blank=True, null=True)
    watched_list = models.ManyToManyField(Movie, related_name='profile_watched_list', blank=True, null=True)

    def __str__(self):
        return f'{ self.account.username } - { self.name }'