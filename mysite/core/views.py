from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RoomDetails,BookingDetails
from django.utils import timezone
from django.http import HttpResponse
from array import *

# Create your views here.
def home(request):
	# data_5=request.POST["data_5"]
	# print(data_5)
	# data_6=request.POST["data_6"]
	# rom=roomdetails(Arrivaldate=data_5,Timeslot=data_6)
	# print("Home page call is made")

	

	# allrooms=RoomDetails.objects.all()
	# print(allrooms)
	# availableslots = []

	# for room in allrooms:
	# 	booking_details=BookingDetails.objects.filter(RoomNo=room.RoomId,BookDate=data_5)
    
	# 	timeslots=[0]*24
 #    # Fill array with 1 meaning the time slot is available.
	# 	for slot in range(room.RoomStarttime,room.RoomEndtime):
	# 		timeslots[slot]=1

	# 	print(timeslots)
    
	# 	print(booking_details)
    
	# 	for booking in booking_details:
	# 		timeslots[booking.BookStarttime] = 0
    
	# 	print(timeslots)
    
	# 	for index in range(0,24):
	# 		if(timeslots[index] == 1):
	# 			availableslots.append(AvailableRoomSlots(room.RoomId, index))


	
	# 		print(availableslots)
	
	# return render(request,'availability2.html',{"available_slots":availableslots })
	return render(request,'bookdate.html')
	
def submitdate(request):
	print("date selected")
	data_5=request.POST["data_5"]
	print(data_5)


	allrooms=RoomDetails.objects.all()
	print(allrooms)
	availableslots = []

	for room in allrooms:
		booking_details=BookingDetails.objects.filter(RoomNo=room.RoomId,BookDate=data_5)
    
		timeslots=[0]*24
    # Fill array with 1 meaning the time slot is available.
		for slot in range(room.RoomStarttime,room.RoomEndtime):
			timeslots[slot]=1

		print(timeslots)
    
		print(booking_details)
    
		for booking in booking_details:
			timeslots[booking.BookStarttime] = 0
    
		print(timeslots)
    
		for index in range(0,24):
			if(timeslots[index] == 1):
				availableslots.append(AvailableRoomSlots(room.RoomId, index))


	
			print(availableslots)

	return render(request,'selecttimeslot.html',{"available_slots":availableslots,"date":data_5 })

def submit(request):
	data_1=request.POST["data_1"]
	data_2=request.POST["data_2"]
	data_3=request.POST["data_3"]
	data_4=request.POST["data_4"]
	data_5=request.POST["data_5"]
	data_6=request.POST["data_6"]
	user=request.user
	print(user)
	print(data_6)
	print(data_5)
	print(data_1)
	print(data_2)
	print(data_3)
	print(data_4)
	res = [int(i) for i in data_6.split() if i.isdigit()] 
	print(res)
	room=RoomDetails.objects.filter(RoomId=res[0])
	# user1=User.objects.filter()


	# room.save()
	print(room)
	booking=BookingDetails(Firstname=data_1,Lastname=data_2,Email=data_4,Phone=data_3,
		BookStarttime=res[1],BookEndtime=res[2],BookDate=data_5,RoomNo=room[0],BookUser=user)
		
	booking.save()
	detail=BookingDetails.objects.filter(Phone=data_3)
		
	return render(request,'details.html',{'bookingdetail':detail})

def submitform(request):
	# print("your form is submitted successfully")
	# data_1=request.POST["data_1"]
	# print(request.POST["data_1"])
	# data_2=request.POST["data_2"]
	# data_3=request.POST["data_3"]
	# data_4=request.POST["data_4"]
	# data_5=request.POST["data_5"]
	# data_6=request.POST["data_6"]
	# data_7=request.POST["data_7"]
	# data_8=request.POST["data_8"]
	# data_9=request.POST["data_9"]

	# room=roomdetails(Firstname=data_1,Lastname=data_2,Phone=data_3,Email=data_4,Numberofadults=data_7,Numberofchildren=data_8,Comments=data_9)
	# room.save()
	# all_details=roomdetails.objects.all()	
	# return render(request,'details.html',{'details' : all_details})
	return render(request,'details.html')
	

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html', {
		'form': form
	})

@login_required
def secret_page(request):
	return render(request,'secret_page.html')


class SecretPage(LoginRequiredMixin,TemplateView):
	template_name='secret_page.html'



def Manager(request):
	return render(request,'Manager.html')

def addroom(request):
	return render(request,'Manager(AddRoom).html')

def roomdetails(request):
	return render(request,'Manager(Room Details).html')

class AvailableRoomSlots:
	RoomId=0
	RoomStarttime=0
	RoomEndtime=0
	def __init__(self,roomId,slotStartTime):
		self.RoomId = roomId
		self.RoomStarttime = slotStartTime
		self.RoomEndtime = slotStartTime + 1
	def __str__(self):
  		return ("RoomNo: {} Starttime: {} Endtime: {}".format(self.RoomId,self.RoomStarttime,self.RoomEndtime) )



	