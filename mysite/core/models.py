from django.db import models

# Create your models here.

class roomdetails(models.Model):
	Firstname=models.CharField(max_length=200)
	Lastname=models.CharField(max_length=200)
	Phone=models.CharField(max_length=200)
	Email=models.CharField(max_length=200)
	Arrivaldate=models.CharField(max_length=200)
	Timeslot=models.CharField(max_length=200)
	Numberofadults=models.IntegerField()
	Numberofchildren=models.IntegerField()
	Comments=models.TextField(max_length=200)
	Starttime=models.IntegerField()
	Endtime=models.IntegerField()

	def __str__(self):
		return self.Firstname


