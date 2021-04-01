#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from User.models import LoginInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginInfo
        fields = ['url', 'AccountName', 'Password']