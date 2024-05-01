from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)
    image=models.ImageField()
    file=models.FileField()

class product(models.Model):
    pass