# Generated by Django 3.1.dev20200224072629 on 2020-03-12 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_bookingdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdetails',
            name='RoomUser',
        ),
    ]