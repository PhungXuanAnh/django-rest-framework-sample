from django.db import models

class Coordinate(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    battery_level = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
