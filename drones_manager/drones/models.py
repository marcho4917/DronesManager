from django.db import models
from django.utils import timezone


class Drone(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    battery_level = models.FloatField()
    current_location = models.CharField(max_length=100)
    last_updated_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

