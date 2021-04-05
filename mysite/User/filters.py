import django_filters
from .models import *

class LoginInfoFilter(django_filters.FilterSet):
    class Meta:
        model = LoginInfo
        fields = ['AccountName']

