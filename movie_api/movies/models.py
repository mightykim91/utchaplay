from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

class Movie(models.Model):
    popularity = models.FloatField(null=True, blank=True)
    video = models.NullBooleanField()
    original_language = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    adult = models.BooleanField()
    poster_path = models.CharField(max_length=300)
    original_title = models.CharField(max_length=200)
    genres_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    vote_count = models.IntegerField(default=0, null=True, blank=True)
    vote_average = models.FloatField(default=0, null=True, blank=True)
    backdrop_path = models.CharField(max_length=300, blank=True)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movie_comment")
    