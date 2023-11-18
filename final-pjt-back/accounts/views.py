from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.
User = get_user_model()


@api_view(['GET'])
def profile(reqeust, username):
    if reqeust.method == 'GET':
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    