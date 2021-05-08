from django.db import models
from django.contrib.auth.models import Group, User


class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # This method for show name of this a row instead of Xxx object(500), ex: Musician object (500)
        return self.name


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instruments = models.ManyToManyField(Instrument)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField()

    def __str__(self):
        # This method for show name of this a row instead of Xxx object(500), ex: Musician object (500)
        return self.first_name + ' ' + self.last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        # This method for show name of this a row instead of Xxx object(500), ex: Musician object (500)
        return self.name + ": " + str(self.release_date)

class Profile(models.Model):
    user = models.OneToOneField(Musician, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    num_stars = models.IntegerField()

    def __str__(self):
        # This method for show name of this a row instead of Xxx object(500), ex: Musician object (500)
        return "Profile of " + self.user.first_name + ' ' + self.user.last_name

    def get_full_address(self):
        return "%s, %s" % (self.street, self.city)
