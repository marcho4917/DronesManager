from django.db import models
from django.utils import timezone


class Drone(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, blank=True)
    battery_level = models.FloatField()
    current_location = models.CharField(max_length=100, blank=True)
    last_updated_time = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

