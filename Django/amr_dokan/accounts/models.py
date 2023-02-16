from django.db import models
from django.contrib.auth.models import  AbstarctUser
# Create your models here.
class CustomUser(AbstarctUser):
    mobile_nuber = models.CharField(max_length=12)
    location = models.CharField(max_length=30)