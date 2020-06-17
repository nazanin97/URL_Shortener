from django.db import models
from django.contrib.auth.models import User



class URL(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	link = models.TextField()
	numberOfVisits = models.IntegerField()
	numberOfUsers = models.IntegerField()

