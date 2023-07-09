from rest_framework import serializers
from .models import Board, BoardUniversity, Comments, BoardDetail, CommentsDetail
from members.models import CustomUser


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body']


class BoardUniversitySerializer(serializers.ModelSerializer):
    user = Board.user
    title = Board.title
    body = Board.body
    university = serializers.CharField(source='user.university', read_only=True)

    class Meta:
        model = BoardUniversity
        fields = ['id', 'user', 'university', 'title', 'body']


class BoardUniversityDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=100, read_only=True)
    body = serializers.CharField(default="", read_only=True)
    university = serializers.CharField(source='user.university', read_only=True)


    class Meta:
        model = BoardUniversity
        fields = ['id', 'user', 'university', 'title', 'body']

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    user = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'post', 'user', 'created_at', 'comment']


class BoardDetailSerializer(serializers.ModelSerializer):
    user = Board.user
    title = Board.title
    body = Board.body
    comments = CommentSerializer(many=True)

    class Meta:
        model = BoardDetail
        fields = ['id', 'user', 'title', 'body', 'comments']


class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    comment = serializers.CharField(source='Comments.comment', read_only=True)

    class Meta:
        model = CommentsDetail
        fields = ['id', 'post', 'user', 'created_at', 'comment']