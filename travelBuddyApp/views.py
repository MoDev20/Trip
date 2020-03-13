from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.db.models import Q
from datetime import date

def register(request):
	return render(request, "index.html")

def createuser(request):
	print(request.POST)
	errors = User.objects.userValidator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/")
	else:
		password = request.POST['pw']
		hashedpassword = bcrypt.hashpw(request.POST ['pw'].encode(), bcrypt.gensalt()).decode()
		newuser = User.objects.create(firstName = request.POST['fname'], lastName = request.POST ['lname'], email = request.POST['useremail'], password = hashedpassword )
		print (newuser.id)
		request.session['loggedInID'] = newuser.id
	return redirect("/travel")

def travels(request):
	loggedUser = User.objects.get(id=request.session['loggedInID'])
	context = {
		"loggedInUser" : loggedUser,
		"myPlannedTrips" : Travel.objects.filter(Q(planner = loggedUser) | Q (join = loggedUser)),
		"allUsersTravelPlans" : Travel.objects.exclude(planner=loggedUser) 
		}
	return render (request, "travels.html", context)

def login(request):
	print(request.POST)
	validationErrors = User.objects.loginValidator(request.POST)
	if len(validationErrors) > 0:
		for key, value in validationErrors.items():
			messages.error(request, value)
		return redirect("/")
	loggedInUser = User.objects.get(email = request.POST['useremail'])
	print("*******")
	print(loggedInUser)
	print("********")
	request.session['loggedInID'] = loggedInUser.id
	return redirect("/travels")

def newtrip(request):
	context = {
		"loggedUser" : User.objects.get(id=request.session['loggedInID'])
	}
	return render(request, "add.html", context)

def addtrip(request):
	print(request.POST)	
	errors = Travel.objects.travelValidator(request.POST)
	if len(errors) > 1:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/travels/add")
	loggedUser = User.objects.get(id=request.session['loggedInID'])
	newTrip = Travel.objects.create(dest = request.POST["dest"], plan = request.POST["plan"], travelStartDate = request.POST["sDate"], travelEndDate = request.POST["eDate"], planner = loggedUser, isJoined = False)
	return redirect("/travels")

def join(request, travelId):
	print(request.POST)
	loggedInUser= User.objects.get(id=request.session['loggedInID'])
	context = {
		"loggedUser" : loggedInUser
	}
	tagged = Travel.objects.get(id= travelId)
	tagged.join.add(loggedInUser)
	return redirect("/travels", context)

def display(request, travelId):
	loggedInUser = User.objects.get(id=request.session['loggedInID'])
	context = {
		"loggedUser" : loggedInUser,
		"travelPlans" : Travel.objects.get(id=travelId),
		"joinedTravelers" : Travel.objects.filter(join = loggedInUser, isJoined = True)
	}
	return render(request, "destination.html", context)

def logout(request):
	request.session.clear()
	return redirect("/")