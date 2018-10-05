from django.db import models
from django.conf import settings



class TextMessage(models.Model):
	talker = models.CharField(max_length=20, blank=False)
	message = models.CharField(max_length=50, blank=True)
	talktime = models.CharField(max_length=10, blank=True)
	def __str__(self):
		return self.talker + " " + self.message
