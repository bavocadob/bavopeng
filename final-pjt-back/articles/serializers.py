from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserSimpleSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_cnt = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id',)

    # comment_set = CommentSerializer(many=True, read_only=True)
    comment_cnt = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = UserSimpleSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'created_at', 'comment_cnt',)