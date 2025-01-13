from django.db import models, connection

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    stock = models.IntegerField()
    daily_ratings = models.FloatField()

    def __str__(self):
        return f"{self.id}"
