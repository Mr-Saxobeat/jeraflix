from django.db import models

class Movie(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
