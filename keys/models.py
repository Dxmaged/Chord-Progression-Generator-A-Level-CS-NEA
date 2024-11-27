from django.db import models
from django.conf import settings

from keys import constants

class Keys(models.Model):
    name = models.CharField(max_length=8)
    tonic = models.CharField(max_length=2)
    tone = models.CharField(blank=True, choices=constants.TONES, max_length=10)

    def __str__(self):
        return self.name