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