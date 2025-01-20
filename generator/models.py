from django.db import models
from django.conf import settings

from generator import constants

class Keys(models.Model):
    name = models.CharField(max_length=8)  # e.g., "C Major"
    tonic = models.CharField(max_length=2)  # e.g., "C", "D", "E"
    tone = models.CharField(choices=constants.TONES, max_length=10, default='Major')  # e.g., "Major", "Minor"

    def __str__(self):
        return self.name
def get_default_key():    
    key = Keys.objects.get(name="C Major")
    scales = Keys.scales.all()

class Scale(models.Model):
    key = models.ForeignKey(Keys, on_delete=models.CASCADE, related_name="scales")
    degrees = models.JSONField()  # e.g., ["C", "D", "E", "F", "G", "A", "B"]


