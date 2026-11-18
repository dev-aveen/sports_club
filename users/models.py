from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=200,null=False,blank=False)
    gym = models.ForeignKey('club.Gym',on_delete=models.CASCADE,related_name='users',null=True,blank=True)

    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name