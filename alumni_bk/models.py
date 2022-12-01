from django.db import models

# Create your models here.

class UsersInfo(models.Model):
    role = models.CharField(max_length=120, primary_key=True)
    course = models.TextField()
    department = models.CharField(max_length=100, null=True)
    year_of_joining = models.TextField(max_length=255)
    year_of_graduation = models.TextField(max_length=255)
    enrollment_no = models.IntegerField()

    def _str_(self):
        return self.role
        
class Event(models.Model):
    title = models.CharField(max_length=120, primary_key=True)
    start_date = models.TextField()
    end_date = models.CharField(max_length=100, null=True)
    start_time = models.TextField(max_length=255)
    end_time = models.TextField(max_length=255)

    def _str_(self):
        return self.title

class Story(models.Model):
    title=models.CharField(max_length=500)
    summary=models.TextField(max_length=3000)
    author=models.CharField(max_length=200)
    day_of_event=models.TextField(max_length=255)
    def _str_(self) :
        return self.title


class Query(models.Model):
    title=models.CharField(max_length=300)
    content = models.CharField(max_length=300)