"""alumni_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alumni_bk.views import RegisterAPI, UserInfoView, EventView, StoryView, QueryView, LoginAPI, LocationView, SkillsView, WExpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register',RegisterAPI.as_view(),name="register"),
    path('api/infoRegister',UserInfoView.as_view(),name="infoRegister"),
    path('api/events',EventView.as_view(),name="Event"),
    path('api/story', StoryView.as_view(),name="Story"),
    path('api/query', QueryView.as_view(),name="query"),
    path('api/login',LoginAPI.as_view(),name="login"),
    path('api/location',LocationView.as_view(),name="location"),
    path('api/skills',SkillsView.as_view(),name="login"),
    path('api/WExpview',WExpView.as_view(),name="login")
]
