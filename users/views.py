from django.shortcuts import render
from rest_framework import generics
from .models import User
from.serializer import UserSerializer
# Create your views here.
# Create a user and display
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    