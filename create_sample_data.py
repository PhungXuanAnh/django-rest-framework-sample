# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from music.models import Album, Musician, Profile, Instrument
import datetime
import time


def randomize_time():
    start = "2021-1-1 00:00:00"
    end = "2021-12-1 00:00:00"
    frmt = '%Y-%m-%d %H:%M:%S'
    stime = datetime.datetime.strptime(start, frmt).replace(tzinfo=datetime.timezone.utc)
    etime = datetime.datetime.strptime(end, frmt).replace(tzinfo=datetime.timezone.utc)
    td = etime - stime
    return random.random() * td + stime

for i in range(0, 56):
    User.objects.create(
        first_name="first_name " + str(i),
        last_name="last_name " + str(i),
        email="test{}@gmail.com".format(i),
        username="username " + str(i)
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
        num_stars=random.randint(0, 1000)
    )


    for j in range(0, 3):
        Album.objects.create(
            artist=musican,
            name="love album " + str(random.randint(0, 1000)),
            release_date=randomize_time(),
            num_stars=random.randint(0, 1000)
        )
