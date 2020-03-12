from django.db import models
from django.contrib.auth.models import User

# Create your models here.



# class AddRoom(models.Model):
# 	RoomId=models.IntegerField()
# 	Starttime=models.ForeignKey(roomdetails,default=0,on_delete=models.SET_DEFAULT,verbose_name="StartEndtime")
# 	Endtime=models.ForeignKey(roomdetails,default=0,on_delete=models.SET_DEFAULT,verbose_name="StartEndtime")
# 	# Username=models.CharField(max_length=100)
# 	IsAvailable=models.BooleanField()

# 	def __str__(self):
# 		return self.RoomId

# 	class Meta:
# 		verbose_name_plural="Add"

class RoomDetailsNew(models.Model):
	RoomId=models.IntegerField()
	RoomStarttime=models.IntegerField()
	RoomEndtime=models.IntegerField()
	RoomUser=models.ForeignKey(User,default=0,on_delete=models.SET_DEFAULT)
	IsRoomAvailable=models.BooleanField()

	def __str__(self):
		return self.RoomId		

# class BookingDetails(models.Model):
# 	Firstname=models.CharField(max_length=200)
# 	Lastname=models.CharField(max_length=200)
# 	Email=models.CharField(max_length=200)
# 	Phone=models.IntegerField(default=0)
# 	Starttime=models.IntegerField()
# 	Endtime=models.IntegerField()
# 	BookUser=models.ForeignKey(User,default=0,on_delete=models.SET_DEFAULT)
# 	RoomNo=models.ForeignKey(RoomDetails,default=0,on_delete=models.SET_DEFAULT)

# 	def __str__(self):
# 		return self.Firstname






