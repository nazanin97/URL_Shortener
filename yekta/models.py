from django.db import models

# Create your models here.
class URL(models.Model):
	link = models.TextField()
	numberOfVisits = models.IntegerField()
	numberOfUsers = models.IntegerField()
		