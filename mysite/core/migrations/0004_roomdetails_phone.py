# Generated by Django 3.1.dev20200224072629 on 2020-03-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_roomdetails_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdetails',
            name='phone',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
