from django.db import models

# Create your models here.
class Student(models.Model):
    # creating name nd rollno
    name = models.CharField(max_length=40)
    roll_no = models.IntegerField()
