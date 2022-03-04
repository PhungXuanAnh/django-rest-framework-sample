# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import sys
import django
import random
import datetime
import time

sys.path.append(os.path.dirname(__file__) + "/../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.local")
django.setup()

# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from music.models import Album, Musician, Profile, Instrument
from coordinate.models import Coordinate
import datetime
import time


def randomize_time():
    start = "2021-1-1 00:00:00"
    end = "2021-12-1 00:00:00"
    frmt = "%Y-%m-%d %H:%M:%S"
    stime = datetime.datetime.strptime(start, frmt).replace(
        tzinfo=datetime.timezone.utc
    )
    etime = datetime.datetime.strptime(end, frmt).replace(tzinfo=datetime.timezone.utc)
    td = etime - stime
    return random.random() * td + stime


for i in range(0, 56):
    User.objects.create(
        first_name="first_name " + str(i),
        last_name="last_name " + str(i),
        email="test{}@gmail.com".format(i),
        username="username " + str(i),
    )

instruments = []
for inst_name in ["piano", "ghita", "organ", "violon"]:
    instruments.append(Instrument.objects.create(name=inst_name))

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
        created_at=randomize_time(),
    )
    musican.instruments.set(instruments)

    Profile.objects.create(
        user=musican,
        age=random.choice(ages),
        street="Street " + str(i),
        city=random.choice(cities),
        num_stars=random.randint(0, 1000),
    )

    for j in range(0, 3):
        Album.objects.create(
            artist=musican,
            name="love album " + str(random.randint(0, 1000)),
            release_date=randomize_time(),
            num_stars=random.randint(0, 1000),
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
