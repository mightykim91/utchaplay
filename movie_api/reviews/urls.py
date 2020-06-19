from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_review_list),
    path('<int:review_pk>/', views.get_review),
    path('create/<int:movie_pk>/', views.create_review),
    path('modify/<int:review_pk>/', views.modify_review),
    path('delete/<int:review_pk>/', views.delete_review),
    # 영화에 해당하는 전체리뷰 가져오기
    path('get_reviews/<int:movie_pk>/',views.get_reviews),
    # 영화:리뷰 => 단일리뷰 가져오기
    path('get_review/<int:review_pk>/', views.get_review),
    # 리뷰별로 댓글 달기
    path('create_comment/<int:review_pk>/',views.create_comment),
    path('get_comments/<int:review_pk>/',views.get_comments),
    path('delete_comment/<int:comment_pk>/',views.delete_comment),

]