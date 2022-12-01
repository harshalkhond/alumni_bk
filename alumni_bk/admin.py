from django.contrib import admin
from .models import UsersInfo , Event , Story, Query, Location, Skills, wExperience
# Register your models here.



admin.site.register(UsersInfo)
admin.site.register(Event)
admin.site.register(Story)
admin.site.register(Query)
admin.site.register(Location)
admin.site.register(Skills)
admin.site.register(wExperience)