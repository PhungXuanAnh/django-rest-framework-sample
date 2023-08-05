# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import sys
import datetime

import django
from celery.schedules import crontab_parser

sys.path.append(os.path.dirname(__file__) + "/../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.local")
django.setup()


# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from main.celery_app import sample_task
from music.models import Album, Musician, Profile
from music.tasks import sample_music_task


def test_hightlight_of_todo_tree_extension():
    # TODO: 
    
    # NOTE:
    
    # [x]
    
    # [ ] 
    # FIXME:
    pass


def test_music_app():
    musican = Musician.objects.get(id=1)
    print(musican.album_set.all())


def test_celery_sample_task():
    # sample_task.apply_async(queue="queue-low")
    # sample_music_task.apply_async(queue="queue-high")
    sample_task.apply_async()
    sample_music_task.apply_async()


def test_crontab_parser():
    print("minutes: ", crontab_parser(60).parse("14,39"))
    print("minutes: ", crontab_parser(60).parse("*/15"))
    print("hours: ", crontab_parser(24).parse("*/4"))
    print("day_of_week: ", crontab_parser(7).parse("*"))
    print("day_of_month: ", crontab_parser(31, 1).parse("*/3"))
    print("months_of_year: ", crontab_parser(12, 1).parse("*/2"))
    print("months_of_year: ", crontab_parser(12, 1).parse("2-12/2"))

    
def steps_to_test_django_model_in_django_shell():
    """ purpose of this work is to see how django convert ORM to SQL"""
    # pip install ipython
    # pip install sqlparse
    # open django shell: python manage.py  shell
    # declare model
    import sqlparse
    from django.db import models
    class Customer(models.Model):
        id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
        age = models.IntegerField(...)
        name = models.CharField(...)

        class Meta:
            db_table = 'Customer'
            managed = False # NOTE: add this config to ignore create real table, reference: https://stackoverflow.com/a/60346675/7639845
            app_label  = "django.contrib.auth", # NOTE: we need to register this model with at least one INSTALLED_APPS, reference: https://stackoverflow.com/a/62772698/7639845 
            
    # now do write your django queryset and print SQL
    qs = Customer.objects.filter(age__gte=25)
    print(qs.query) # reference: https://stackoverflow.com/a/1074224/7639845
    print("---------------------------------")
    print(sqlparse.format(str(qs.query), reindent=True, keyword_case='upper'))
   
 
def test_select_related_and_prefetch_related_real_sql():
    from django.db import models
    import sqlparse
    
    class ModelA(models.Model):
        class Meta:
            db_table = 'ModelA'
            managed = False # NOTE: add this config to ignore create real table, reference: https://stackoverflow.com/a/60346675/7639845
            app_label  = "django.contrib.auth", # NOTE: we need to register this model with at least one INSTALLED_APPS, reference: https://stackoverflow.com/a/62772698/7639845 
        

    class ModelB(models.Model):
        a = models.ForeignKey(ModelA, on_delete=models.CASCADE)
        class Meta:
            db_table = 'ModelB'
            managed = False # NOTE: add this config to ignore create real table, reference: https://stackoverflow.com/a/60346675/7639845
            app_label  = "django.contrib.auth", # NOTE: we need to register this model with at least one INSTALLED_APPS, reference: https://stackoverflow.com/a/62772698/7639845 
        

    print("Forward ForeignKey relationship")
    b = ModelB.objects.select_related('a').all()
    print(sqlparse.format(str(b.query), reindent=True, keyword_case='upper'))
    print("----------------------------------------------------------------")

    print("Reverse ForeignKey relationship")
    a = ModelA.objects.prefetch_related('modelb_set').all()
    print(sqlparse.format(str(a.query), reindent=True, keyword_case='upper'))
    
    from django.db import connection
    print(connection.queries)
    # b.objects.select_related('a').first()

if __name__ == "__main__":
    # test_celery_sample_task()
    # test_crontab_parser()
    # steps_to_test_django_model_in_django_shell()
    test_select_related_and_prefetch_related_real_sql()
