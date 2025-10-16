from django.db import models

# Create your models here.
class Employee(models.Model):
    # creating differnet columns names nd the type  tht can be added in it 
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
