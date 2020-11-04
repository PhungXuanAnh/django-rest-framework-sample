# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from music.models import Album, Musician, Profile, Instrument
import datetime


for i in range(0, 56):
    User.objects.create(
        first_name="first_name " + str(i),
        last_name="last_name " + str(i),
        email="test{}@gmail.com".format(i),
        username="username " + str(i)
    )

instruments = []
for i in range(0, 5):
    instruments.append(Instrument.objects.create(name="instrument " + str(1)))

for i in range(0, 56):
    musican = Musician.objects.create(
        first_name="first_name " + str(i),
        last_name="last_name " + str(i)
    )
    musican.instruments.set(instruments)
    Profile.objects.create(
        user=musican,
        street="Street " + str(i),
        city="City " + str(i)
    )


    for i in range(0, 5):
        Album.objects.create(
            artist=musican,
            name="love " + str(i),
            release_date=datetime.datetime.now(),
            num_stars=100
        )


