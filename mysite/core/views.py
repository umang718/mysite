from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import roomdetails
from django.utils import timezone
from django.http import HttpResponse
from array import *

# Create your views here.
def home(request):
	# data_5=request.POST["data_5"]
	# data_6=request.POST["data_6"]
	# rom=roomdetails(Arrivaldate=data_5,Timeslot=data_6)
	print("Home page call is made")

	# Get the details form the room_details.
	# room=roomdetails(Firstname="nikunj", 
	# 	Lastname="sorathiya",
	# 	Phone="a",
	# 	Email="af",
	# 	Numberofadults=1,Numberofchildren=0,
	# 	Comments="f",
	# 	Arrivaldate=timezone.now(),
	# 	Starttime=3,
	# 	Endtime=4)
	# room.save()
	booked_timeSlots = roomdetails.objects.all()

	# fill in available time slots.
	# 
	timeslot_byhour = [0]*24
	for row in booked_timeSlots:
		for hour in range(row.Starttime,row.Endtime):
			timeslot_byhour[hour]=1
	print(timeslot_byhour)
	timeslot_byhour_string = [];
	for hour in range(len(timeslot_byhour)):
		if (timeslot_byhour[hour]==1):
			timeslot_byhour_string.append({"Starttime": hour, "string":"{}-{}".format(hour,hour+1)})
	print(timeslot_byhour_string)
	return render(request,'availability2.html')

def submit(request):
	return render(request,'home.html')

def submitform(request):
	print("your form is submitted successfully")
	data_1=request.POST["data_1"]
	print(request.POST["data_1"])
	data_2=request.POST["data_2"]
	data_3=request.POST["data_3"]
	data_4=request.POST["data_4"]
	data_5=request.POST["data_5"]
	data_6=request.POST["data_6"]
	data_7=request.POST["data_7"]
	data_8=request.POST["data_8"]
	data_9=request.POST["data_9"]

	room=roomdetails(Firstname=data_1,Lastname=data_2,Phone=data_3,Email=data_4,Numberofadults=data_7,Numberofchildren=data_8,Comments=data_9)
	room.save()
	all_details=roomdetails.objects.all()	
	return render(request,'details.html',{'details' : all_details})
	

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


# def index(request):
# 	all_details=roomdetails.objects.all()
# 	return render(request,'details.html',{details : all_details})