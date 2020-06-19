from rest_framework import serializers
from .models import Review,ReviewComment
from accounts.serializers import UserSerializer



class ReviewListSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'user','rank']
        read_only_fields = ['user','id']
       

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    # 유저정보를 넣으면 username 이 보이는데 게시물 수정이 안됨!!

    class Meta:
        model = Review
        fields = ['id','title','content','user','rank','created_at','updated_at']
        read_only_fields = ['user','id']

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        # user = UserSerializer()

        model = ReviewComment
        fields = ['content','user','id']
        # fields = '__all__'
        read_only_fields = ['user','id']

class ReviewCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        # user = UserSerializer()

        model = ReviewComment
        # fields = ['content']
        fields = '__all__'
        read_only_fields = ['user','review_id']