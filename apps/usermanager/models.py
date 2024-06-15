from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_type=models.CharField(max_length=30,blank=False)
    authentication_token=models.CharField(max_length=16,editable=False,blank=False)


    def __str__(self):
        return self.username
    

class APILog(models.Model):
    username=models.CharField(max_length=150,blank=False)
    timestamp=models.DateTimeField()

    def __str__(self):
        return f"{self.username} - {self.timestamp}"