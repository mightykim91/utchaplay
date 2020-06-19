from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Review,ReviewComment
from movies.models import Movie
from .serializers import ReviewSerializer, ReviewCommentSerializer,ReviewListSerializer, ReviewCommentListSerializer


# 영화:리뷰 => 단일리뷰 가져오기
@api_view(['GET'])
def get_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
    

@api_view(['GET'])
def get_review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(movie=movie, user=request.user)
        return Response(status=201)
    return Response(status=400)


@api_view(['PUT'])
def modify_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewListSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)
    return Response(status=400)


@api_view(['POST'])
def delete_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response(status=200)

@api_view(['GET'])
def get_reviews(request, movie_pk):
    reviews = Review.objects.filter(movie = movie_pk).order_by('-pk')
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# 리뷰별로 댓글 달기
@api_view(['POST'])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        serializer.save(review_id=review, user=user)
        return Response(serializer.data)
    return Response(serializer.errors)
    


@api_view(['GET'])
def get_comments(request,review_pk):
    reviewcomments = ReviewComment.objects.filter(review_id=review_pk).order_by('-pk')
    serializer = ReviewCommentListSerializer(reviewcomments,many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_comment(reqeust, comment_pk):
    comment = get_object_or_404(ReviewComment, pk=comment_pk)
    comment.delete()
    return Response(status=200)
