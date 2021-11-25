from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from users.models import UserModel
from users.serializers import UserSerializer, UserListSerializer


class UserViewSet(viewsets.ViewSet):
    def insert_user(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        users_serializer = UserListSerializer(data=user_serializer.data)
        users_serializer.is_valid(raise_exception=True)

        return Response(users_serializer.data, status.HTTP_200_OK)

    def list_users(self, request):
        users = UserModel.objects.all()
        users_list_serializer = UserListSerializer(users, many=True)

        return Response(users_list_serializer.data, status.HTTP_200_OK)

    def get_user(self, request, user_id):
        user = UserModel.objects.filter(pk=user_id).first()
        users_serializer = UserListSerializer(user)

        return render(request, 'user.html', users_serializer.data)
