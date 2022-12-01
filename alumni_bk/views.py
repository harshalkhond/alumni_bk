from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer,UserInfoSerializer,UserSerializer, EventSerializer , StorySerializer , LocationSerializer , SkillsSerializer , WExpSerializer
from .serializers import QuerySerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from rest_framework.views import APIView
from .models import UsersInfo , Event , Story,Query,Location,Skills,wExperience
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from django.contrib.auth import login
from django.contrib.auth.models import User
# Create your views here.
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserInfoView(APIView):
    def get(self, request, *args, **kwargs):
        result = UsersInfo.objects.all()
        serializers = UserInfoSerializer(result, many=True)
        return Response({'status': 'success', "Data": serializers.data}, status=200)

    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Data": serializer.data}, status=200)

        else:
            return Response({"status": "error", "Data": serializer.errors}, status=400)


class EventView(APIView):
    def get(self, request, *args, **kwargs):
        result = Event.objects.all()
        serializers = EventSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Data": serializer.data}, status=200)

        else:
            return Response({"status": "error", "Data": serializer.errors}, status=400)



class StoryView(APIView):
    def get(self, request, *args, **kwargs):
        result = Story.objects.all()
        serializers = StorySerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Data": serializer.data}, status=200)

        else:
            return Response({"status": "error", "Data": serializer.errors}, status=400)


class QueryView(APIView):
    def get(self, request, *args, **kwargs):
        result = Query.objects.all()
        serializers = QuerySerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Data": serializer.data}, status=200)

        else:
            return Response({"status": "error", "Data": serializer.errors}, status=400)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class LocationView(APIView):
    def get(self, request, *args, **kwargs):
        result = Location.objects.all()
        serializers = LocationSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Data": serializer.data}, status=200)

        else:
            return Response({"status": "error", "Data": serializer.errors}, status=400)



class SkillsView(APIView):
    def get(self, request, *args, **kwargs):
        result = Skills.objects.all()
        serializers = SkillsSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = SkillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Data": serializer.data}, status=200)

        else:
            return Response({"status": "error", "Data": serializer.errors}, status=400)


class WExpView(APIView):
    def get(self, request, *args, **kwargs):
        result = wExperience.objects.all()
        serializers = WExpSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = WExpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Data": serializer.data}, status=200)

        else:
            return Response({"status": "error", "Data": serializer.errors}, status=400)