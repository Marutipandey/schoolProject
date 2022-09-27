import email
from operator import mod
from django.db import models

# Create your models here.
class studentDetails(models.Model):
    Name=models.CharField(max_length=100)
    Father_name=models.CharField(max_length=100)
    Mother_name=models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Class = models.IntegerField()
    Contact_number =models.IntegerField()
    Address = models.CharField(max_length=300)
    
