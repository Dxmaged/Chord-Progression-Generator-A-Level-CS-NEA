from django.db import models
from django.conf import settings

from keys import constants

class Keys(models.Model):
    name = models.CharField(max_length=8)  # e.g., "C Major"
    tonic = models.CharField(max_length=2)  # e.g., "C", "D", "E"
    tone = models.CharField(choices=constants.TONES, max_length=10)  # e.g., "Major", "Minor"

    def __str__(self):
        return self.name
    
class Scale(models.Model):
    tone = 

    def __str__(self):
        return f"{self.key.name} Scale"