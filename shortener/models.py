from django.db import models

# Create your models here.

class Url(models.Model):

	link = models.CharField(max_length=100)
	uuid = models.CharField(max_length=5)

	def __str__(self):
		return f"{self.link} ({self.uuid})"
