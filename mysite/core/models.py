from django.db import models

# Create your models here.

class RoomDetails1(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	arrivaldate=models.DateField()
	timeslot=models.CharField(max_length=200)
	numberofadults=models.CharField(max_length=50)
	numberofchildren=models.CharField(default=0,max_length=50)
	comments=models.TextField(max_length=500)

	def __str__(self):
		return self.firstname 
