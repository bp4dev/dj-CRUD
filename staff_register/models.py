from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    staff_number = models.CharField(max_length=100)
   # EmailField = models.EmailField
    position = models.ForeignKey(Position, on_delete=models.CASCADE)