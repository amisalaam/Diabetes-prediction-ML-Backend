from django.shortcuts import render
from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCreateSerializers
from django.contrib.auth import get_user_model

User = get_user_model()



# Create your views here.

class RegisterView(APIView):
    def post (self,request):
        data = request.data
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']

        user = User.objects.create_user(first_name,last_name,email,password)
        serializers = UserCreateSerializers(user)

        return Response(serializers.data, status=status.HTTP_201_CREATED)


class GetUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        pass