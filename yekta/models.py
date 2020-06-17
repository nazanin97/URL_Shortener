from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class URL(models.Model):
	link = models.TextField()
	numberOfVisits = models.IntegerField()
	numberOfUsers = models.IntegerField()
	

# class User