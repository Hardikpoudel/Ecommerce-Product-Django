from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class userDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class userAddress(models.Model):
    userID = models.ForeignKey(userDetails, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
