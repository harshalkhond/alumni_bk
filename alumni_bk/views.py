from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer,UserInfoSerializer,UserSerializer, EventSerializer , StorySerializer
from .serializers import QuerySerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from rest_framework.views import APIView
from .models import UsersInfo , Event , Story,Query
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