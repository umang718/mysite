# Generated by Django 3.1.dev20200224072629 on 2020-03-12 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20200312_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Phone', models.IntegerField(default=0)),
                ('BookStarttime', models.IntegerField()),
                ('BookEndtime', models.IntegerField()),
                ('BookDate', models.DateField()),
                ('BookUser', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('RoomNo', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.RoomDetails')),
            ],
        ),
    ]
