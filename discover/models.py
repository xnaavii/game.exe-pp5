from django.db import models

from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title