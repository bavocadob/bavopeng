from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Profile
from .serializers import ProfileSerializer, ProfileFormSerializer, UserFollowSerializer, UserProfileSerializer

# Create your views here.
User = get_user_model()


# 프로필 조회, 수정
@api_view(['GET', 'PUT'])
def profile(reqeust, username):
    user = get_object_or_404(User.objects.select_related('profile').prefetch_related('liked_movies', 'disliked_movies', 'wished_movies', 'liked_articles', 'disliked_articles'), username=username)
    profile = user.profile

    if reqeust.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    elif reqeust.method == 'PUT':
        if reqeust.user.is_authenticated and reqeust.user.profile == profile:
            serializer = ProfileFormSerializer(profile, data=reqeust.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            data = {'detail': 'Authentication credentials were not provided.'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        

# 팔로잉 조회, 팔로우, 언팔로우
@api_view(['GET', 'POST'])
def following(request, user_pk):
    target_user = get_object_or_404(User, pk=user_pk)
    request_user = request.user

    if request.method == 'GET':
        following_list = target_user.followings.all()
        serializer = UserFollowSerializer(following_list, many=True)
        return Response(serializer.data)

    elif request.user.is_authenticated and request_user != target_user:
        if request.method == 'POST':
            if request_user.followings.filter(pk=user_pk).exists():
                request_user.followings.remove(target_user)
            else:
                request_user.followings.add(target_user)
            return Response(status=status.HTTP_200_OK)
        
    else:
        data = {'detail': 'Authentication credentials were not provided.'}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
    

# 팔로워 조회
@api_view(['GET'])
def follower(request, user_pk):
    target_user = get_object_or_404(User, pk=user_pk)
    follower_list = target_user.followers.all()
    serializer = UserFollowSerializer(follower_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def exists_id(request):
    username = request.GET.get('username', '')
    if User.objects.all().filter(username=username).exists():
        return Response({'result':True})
    else:
        return Response({'result':False})
    

@api_view(['Get'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    user_info = User.objects.get(pk=user.pk)
    serializer = UserProfileSerializer(user_info)
    return Response(serializer.data)