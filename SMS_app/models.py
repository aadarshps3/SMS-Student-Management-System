from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='teacher')
    Name = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=10)
    Address = models.CharField(max_length=255)
    Email_Id = models.EmailField()
    Photo = models.ImageField(upload_to='photo')
    Id_Card = models.FileField(upload_to='id')

    def __str__(self):
        return self.Name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="customer")
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=10)
    Email_Id = models.EmailField()
    Photo = models.ImageField(upload_to='pic')
    Id_Card = models.FileField(upload_to='Id')


    def __str__(self):
        return self.Name