from django.db import models
from django.contrib.auth.models import User



class URL(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	link = models.TextField()
	shortLink = models.TextField(default='')
	numberOfVisits = models.IntegerField(default=0)
	numberOfUsers = models.IntegerField(default=0)
	numFirefox = models.IntegerField(default=0)
	numChrome = models.IntegerField(default=0)
	numSafari = models.IntegerField(default=0)


