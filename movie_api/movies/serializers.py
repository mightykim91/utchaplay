from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie, Comment, Genre
from accounts.serializers import UserSerializer

class MovieListSerializer(serializers.ModelSerializer):
    # genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        # fields = "__all__"
        fields = ['id', 'overview','adult','title','release_date','poster_path','genres_ids','original_title']

class MovieSerializer(serializers.ModelSerializer):
    # genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'overview','adult','title','release_date','poster_path','genres_ids','original_title']
        read_only_fields = ['id','genre_ids']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content','user','id']
        read_only_fields = ['user','id']

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user','movie_id']

class GenreListSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['genre_name','movies']
        # read_only_fields = ['user']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    genres_ids = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

