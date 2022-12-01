from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UsersInfo , Event , Story, Query
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersInfo
        fields = ['role','course','department','year_of_joining','year_of_graduation','enrollment_no','name','email','pass_year','city','state','country','pass_year','city','state','country']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title','start_date','end_date','start_time','end_time']

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['title','summary','author','day_of_event']

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['title','content']