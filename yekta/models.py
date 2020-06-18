from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class URL(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	link = models.TextField()
	shortLink = models.TextField(default='')
	numberOfVisits = models.IntegerField(default=0)
	numberOfUsers = models.IntegerField(default=0)
	numFirefox = models.IntegerField(default=0)
	numChrome = models.IntegerField(default=0)
	numSafari = models.IntegerField(default=0)
	numMobile = models.IntegerField(default=0)
	numDesktop = models.IntegerField(default=0)


class RequestLog(models.Model):
	link = models.TextField(default='')
	ip = models.CharField(max_length=16)
	time = models.DateTimeField(default=timezone.now)
	browser = models.CharField(max_length=7)
	device = models.CharField(max_length=7)
	