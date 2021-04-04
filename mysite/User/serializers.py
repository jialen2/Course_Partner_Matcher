#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from User.models import Enrollment
#from User.models import Courses


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['url', 'NetId', 'CRN']

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Courses
#         fields = ['CRN', 'CourseTitle', 'CourseNumber', 'Department', 'Section', 'ScheduleType', 'Instructor', 'MeetingTime']