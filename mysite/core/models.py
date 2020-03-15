from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RoomDetails(models.Model):
	RoomId=models.IntegerField()
	RoomStarttime=models.IntegerField()
	RoomEndtime=models.IntegerField()
	IsRoomAvailable=models.BooleanField()

	def __str__(self):
		return "{}".format(self.RoomId)		


class BookingDetails(models.Model):
	Firstname=models.CharField(max_length=200)
	Lastname=models.CharField(max_length=200)
	Email=models.CharField(max_length=200)
	Phone=models.IntegerField(default=0)
	BookStarttime=models.IntegerField()
	BookEndtime=models.IntegerField()
	BookDate=models.DateField()
	BookUser=models.ForeignKey(User,default=0,on_delete=models.SET_DEFAULT)
	RoomNo=models.ForeignKey(RoomDetails,default=0,on_delete=models.SET_DEFAULT)

	def __str__(self):
		return self.Firstname






