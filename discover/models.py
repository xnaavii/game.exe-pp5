from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    thumbnail_url = models.URLField(blank=True, null=True)
    rating = models.FloatField(default=0.0)
    platforms = models.ManyToManyField(Platform, blank=True)

    def __str__(self):
        return self.title
