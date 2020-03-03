from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RoomDetails
#from django.http import HttpResponse


# Create your views here.
def home(request):
	return render(request,'home.html')


def submitdetails(request):
	print("form is submitted successfully")
	firstname=request.POST["data_2"]
	lastname=request.POST["data_3"]
	email=request.POST["data_5"]
	phone=request.POST["data_4"]
	
	arrivaldate=request.POST["data_6"]
	timeslot=request.POST["data_7"]
	adults=request.POST["data_8"]
	children=request.POST["data_9"]
	comments=request.POST["data_10"]

	roomdetails1=RoomDetails(data_2=firstname,data_3=lastname,data_4=phone,data_5=email,data_6=arrivaldate,data_7=timeslot,
		data_8=adults,data_9=children,data_10=comments)
	roomdetails1.save()
	return render(request,'home.html')

	

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