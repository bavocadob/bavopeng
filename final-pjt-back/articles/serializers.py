from rest_framework import serializers
from django.contrib.auth import get_user_model
# from accounts.models import Profile
from accounts.serializers import UserProfileSerializer
from .models import Article, Comment
from bs4 import BeautifulSoup
from movies.models import Movie

 

# 전체 게시글
class ArticleListSerializer(serializers.ModelSerializer):
    comment_cnt = serializers.IntegerField(source='comments.count', read_only=True)
    liked_cnt = serializers.IntegerField(source='liked_by.count', read_only=True)
    user = UserProfileSerializer(read_only=True)
    has_image = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'created_at', 'comment_cnt', 'liked_cnt', 'has_image')

    def get_has_image(self, obj):
        soup = BeautifulSoup(obj.content, 'html.parser')
        return bool(soup.find('img'))


# 댓글 조회
class CommentSerializer(serializers.ModelSerializer):
    class UserIDSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id',)

    user = UserProfileSerializer(read_only=True)
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    replies = serializers.SerializerMethodField()
    liked_cnt = serializers.IntegerField(source='liked_by.count', read_only=True)
    liked_by = UserIDSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'article', 'parent_comment', 'content', 
                    'created_at', 'updated_at', 'replies', 'liked_cnt', 'liked_by')
    
    # 대댓글 가져오기
    def get_replies(self, obj):
        if obj.replies:
            return CommentSerializer(obj.replies, many=True).data


# 단일 게시글 조회
class ArticleSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'rating_avg', 'release_date')

    user = UserProfileSerializer(read_only=True)
    # comments = serializers.SerializerMethodField()
    comment_cnt = serializers.IntegerField(source='comments.count', read_only=True)
    like_cnt = serializers.IntegerField(source='liked_by.count', read_only=True)
    dislike_cnt = serializers.IntegerField(source='disliked_by.count', read_only=True)
    ref_movie = MovieSerializer(read_only=True)
    is_like = serializers.SerializerMethodField()
    is_dislike = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'image', 'ref_movie', 'created_at', 'updated_at', 
                  'like_cnt', 'dislike_cnt', 'comment_cnt', 'is_like', 'is_dislike')
        
    def get_is_like(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.liked_by.filter(id=user.id).exists()
        return False

    def get_is_dislike(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.disliked_by.filter(id=user.id).exists()
        return False

    # 부모 댓글만 가져오기
    # def get_comments(self, obj):
    #     comments = CommentSerializer(obj.get_parent_comments(), many=True, read_only=True).data
    #     return comments


# 단일 게시글 작성, 수정
class ArticleFormSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Article
        # ManyToMany Field 제외
        fields = ('id', 'user', 'ref_movie', 'title', 'content', 'image', 'created_at', 'updated_at')


# 댓글 작성, 수정
class CommentFormSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'user', 'article', 'parent_comment', 'content', 'created_at', 'updated_at',)