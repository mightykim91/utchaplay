from django.forms import ModelForm
from .models import Genre, Movie, Comment

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ['like_users',]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]