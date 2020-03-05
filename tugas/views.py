from django.shortcuts import render,redirect
from django.http import HttpResponse
#
# Import all models
#
from .models import *

# Create your views here.

#
# Views for index.html
#
def home(request):
    return render(request,'pages/index.html')
#
# Views for cars.html
#
def cars(request):
    result = "<tr><td>"
    #
    # Retrieve all objects in the table
    #
    cars = Car.objects.all()
    #
    # Put the car details into the result
    #
    for car in cars:
        result += "Car name: " + car.carName + "<br>" + "Car category: " + car.carCategory + "<br>" + "Car year: " + car.carYear + "<br>" + "Car city: " + car.carCity + "<br>" + "Car price: " + car.carPrice + "<br>" + "Car description: " + car.carDescription + "<br><br>"
    #
    # Condition for no car found
    #
    if result == "<tr><td>":
        result += "Car not found"
    result += "</td></tr>"
    response = {
        'result' : result
    }
    return render(request, 'pages/cars.html', response)
#
# Views for carsView.html
#
def carsView(request):
    return render(request, 'pages/carsView.html')
#
# Views for about.html
#
def about(request):
    return render(request, 'pages/about.html')
#
# Views for articles.html
#
def articles(request):
    return render(request, 'pages/articles.html')

#
# Views for finding car based on car's name
#
def findCar(request):
    #
    # Retrieve the search query
    #
    target = request.POST['carName']
    result = "<tr><td>"
    #
    # Retrieve all objects in the table
    #
    cars = Car.objects.all()
    #
    # Put the car details into the result
    #
    for car in cars:
        if target == car.carName:
            result += "Car name: " + car.carName + "<br>" + "Car category: " + car.carCategory + "<br>" + "Car year: " + car.carYear + "<br>" + "Car city: " + car.carCity + "<br>" + "Car price: " + car.carPrice + "<br>" + "Car description: " + car.carDescription + "<br>"
    #
    # Condition for no car found
    #
    if result == "<tr><td>":
        result += "Car not found"
    result += "</td></tr>"
    response = {
        'result' : result
    }
    return render(request, 'pages/carResult.html', response)
