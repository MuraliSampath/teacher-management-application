from django.db import models
from django.core.validators import MinLengthValidator

class Teacher(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.CharField(max_length=100)
    numberOfClass = models.IntegerField()