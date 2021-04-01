#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from User.serializers import UserSerializer
from User.models import LoginInfo


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LoginInfo.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]