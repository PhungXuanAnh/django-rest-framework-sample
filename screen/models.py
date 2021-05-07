from django.db import models


class UnlockScreenUrl(models.Model):
    url = models.CharField(max_length=50)
