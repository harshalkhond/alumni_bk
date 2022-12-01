from django.contrib import admin
from .models import UsersInfo , Event , Story, Query
# Register your models here.



admin.site.register(UsersInfo)
admin.site.register(Event)
admin.site.register(Story)
admin.site.register(Query)