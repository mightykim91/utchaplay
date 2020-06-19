from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
# from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import GenreSerializer
from .models import Genre, Movie, Comment
from .serializers import MovieSerializer, MovieListSerializer, GenreListSerializer, CommentSerializer,CommentListSerializer
from .serializers import RecommendationSerializer

# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse


# Create your views here.
API_KEY = '611b17e08929eff3b420b33f2d24c4bb'

@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    print(genre)
    movies = Movie.objects.filter(genres_ids=genre).all()
    print(movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def add_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)

@api_view(['DELETE'])
def delete_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return Response(status=200)

@api_view(['PUT'])
def modify_movie(request, movie_pk):
    movie =  get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)

def like(request):
    pass

@api_view(['GET'])
def get_genre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_genre(request):
    serializer = GenreListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)
    
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def delete_genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    genre.delete()
    return Response(status=200)
    

@api_view(['PUT'])
def modify_genre(request, genre_pk):
    genre =  get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreListSerializer(genre, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)


@api_view(['POST'])
def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        serializer.save(movie_id=movie, user=user)
        return Response(serializer.data)
    

@api_view(['GET'])
def get_comments(request,movie_pk):
    comments = Comment.objects.filter(movie_id=movie_pk).order_by('-pk')
    serializer = CommentListSerializer(comments,many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_comment(reqeust, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=200)


@api_view(['POST'])
def like(request, movie_pk):
    print(request.user)
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(id=user.pk).exists():
        movie.like_users.remove(user)
        liked = False

    else:
        movie.like_users.add(user)
        liked = True

    context = {
        'liked': liked,
        #'count': like_movies
    }

    return JsonResponse(context)


@api_view(['GET'])
def checkLike(request, movie_pk):
    user = request.user
    print(user)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(id=request.user.pk).exists():
        print('yes')
        liked = True
    else:
        liked = False
        print('no')
    context = {
        'liked': liked,
    }
    return JsonResponse(context)


#추천 알고리즘
@api_view(['GET'])
def recommendation(request):
    user = request.user
    #유저가 좋아한 영화의 장르 추출
    like_genres = set()  # 중복제거위해 set 사용
    if user.like_movies.exists():
        for movie in user.like_movies.all():
            #print(movie.genres_ids.values('id'))
            for genre in movie.genres_ids.all().values('id'):
                like_genres.add(genre['id'])
        print(like_genres)

        #좋아하는 장르별 영화 추천(좋아요 눌러진순)
        genre_dict = {}
        for genre in like_genres:
            name = get_object_or_404(Genre, pk=genre)
            movies = Movie.objects.annotate(num_like_users=Count(
                'like_users')).filter(genres_ids=genre).all()[:8]
            serializer = RecommendationSerializer(movies, many=True)
            genre_dict[name.genre_name] = serializer.data
            #print(genre_dict)
        #genre_dict = genre_dict
        return JsonResponse(genre_dict)

    #좋아요 누른 영화가 없을 경우
    else:
        genre_dict = {}
        for genre in Genre.objects.all():
            print(genre.id, genre.genre_name)
            movies = Movie.objects.annotate(num_like_users=Count('like_users')).filter(genres_ids=genre.id).all()[:8]
            serializer = MovieListSerializer(movies, many=True)
            genre_dict[genre.genre_name] = serializer.data
        return JsonResponse(genre_dict)

        