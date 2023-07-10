from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=64, null=True)
    birth = models.DateField(null=True)
    email = models.CharField(max_length=64, null=True)
    registration_time = models.DateTimeField(auto_now_add=True)
