from rest_framework import generics
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import get_user_model

from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        invited = get_user_model().objects.filter(rec_code=user.code).count()
        return Response({
        'name': user.name,
        'code': user.code,
        'token': token[1],
        'invited': invited,
        })

class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)
        invited = get_user_model().objects.filter(rec_code=user.code).count()
        return Response({
            'name': user.name,
            'code': user.code,
            'token': token[1],
            'invited': invited,
        })


class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [
    permissions.IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user