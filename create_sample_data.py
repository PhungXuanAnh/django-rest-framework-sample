# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import django
import random
import datetime
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from music.models import Album, Musician, Profile, Instrument
from coordinate.models import Coordinate


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

cities = ["Hanoi", "HCM", "HaiPhong", "Hue", "Danang"]
ages = [20, 30, 40, 50]
first_names = ["Phung", "Pham", "Phan", "Nguyen", "Le", "Anh"]
last_names = ["Anh", "Hoang", "Tho", "Hoa", "Nghia", "Sao", "Hai", "Thao"]
for i in range(0, 500):
    musican = Musician.objects.create(
        first_name=random.choice(first_names),
        last_name=random.choice(last_names),
        email="example_{}@gmail.com".format(i),
        password="123456" + str(i),
    )
    musican.instruments.set(instruments)
    Profile.objects.create(
        user=musican,
        age=random.choice(ages),
        street="Street " + str(i),
        city=random.choice(cities),
        num_stars=random.randint(0, 1000)
    )


    for i in range(0, 3):
        Album.objects.create(
            artist=musican,
            name="love " + str(i),
            release_date=datetime.datetime.now(),
            num_stars=100
        )

coordinates = [
    "20.973962519591822, 105.77874754205386",
    "20.97973842975352, 105.785519125676",
    "20.9929949412513, 105.80121475550659",
    "20.99646554261962, 105.80926909186702",
    "21.005189892461825, 105.81882070870473"
]
for coordinate in coordinates:
    lat, lng = coordinate.split(', ')
    Coordinate.objects.create(
        latitude=lat,
        longitude=lng
    )
    time.sleep(1)