from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name = 'index'),
    path('<int:genre_pk>/', views.movie_genre, name='movie_genre'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('delete_movie/<int:movie_pk>/',views.delete_movie, name='delete_movie'),
    path('modify_movie/<int:movie_pk>/',views.modify_movie, name='modify_movie'),
    path('<int:movie_id>/like/', views.like, name='like'),
    path('getgenres/', views.get_genre),
    path('add_genre/', views.add_genre, name='add_genre'),
    path('delete_genre/<int:genre_pk>/',views.delete_genre, name='delete_genre'),
    path('modify_genre/<int:genre_pk>/',views.modify_genre, name='modify_genre'),
    path('create_comment/<int:movie_pk>/',views.create_comment, name="create_comment"),
    path('get_comments/<int:movie_pk>/', views.get_comments),
    path('delete_comment/<int:comment_pk>/',views.delete_comment),
    path('like/<int:movie_pk>/', views.like),
    path('checklike/<int:movie_pk>/', views.checkLike),
    path('recommendation/', views.recommendation)

    ]
