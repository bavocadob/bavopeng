from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Profile
from .serializers import ProfileSerializer, ProfileFormSerializer

# Create your views here.
User = get_user_model()


# 프로필 조회, 수정
@api_view(['GET', 'PUT'])
def profile(reqeust, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile

    if reqeust.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    elif reqeust.method == 'PUT':
        if reqeust.user.is_authenticated and reqeust.user.profile == profile:
            serializer = ProfileFormSerializer(profile, data=reqeust.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            data = {"detail": "Authentication credentials were not provided."}
            return Response(data, status=status.HTTP_403_FORBIDDEN)