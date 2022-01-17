from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Movie(models.Model):
    imdb_id = models.CharField(max_length=12, null=True)
    imdb_rating = models.CharField(max_length=3, blank=True, null=True)
    poster_link = models.CharField(max_length=280, blank=True, null=True)
    poster_low = models.CharField(max_length=280, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100, null=True)
    year = models.PositiveSmallIntegerField(
        default=current_year(),
        validators=[MinValueValidator(1878), max_value_current_year],
    )
    director = models.CharField(max_length=100, null=True)
    genres = models.CharField(max_length=100, null=True)

    def serialize(self):
        return {
            'id':self.id,
            'imdb_id':self.imdb_id,
            'title':self.title,
            'rating':self.imdb_rating,
            'plot':self.plot,
            'poster_link':self.poster_link,
            'poster_low':self.poster_low,
            'year':self.year,
            'director':self.director,
            'genres':self.genres
        }

    def __str__(self):
        return f'{self.title} - ({self.year})'
