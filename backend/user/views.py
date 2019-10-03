from django.contrib.auth import get_user_model
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class RetrieveUserView(generics.RetrieveAPIView):
    """Get the data for a single user from the database"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
