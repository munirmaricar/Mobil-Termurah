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
    #
    # Retrieve all objects in the table
    #
    cars = Car.objects.all()
    response = {
        'cars' : cars
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
    #
    # Retrieve all car objects in the database
    #
    articles = Article.objects.all()
    response = {
        'articles' : articles
    }
    return render(request, 'pages/articles.html', response)
#
# Views for choosing article
#
def chooseArticle(request):
    #
    # Retrieve the search query
    #
    target = request.POST['articleTitle']
    #
    # Retieve all article object in the database
    #
    articles = Article.objects.all()
    response = {
        'articles' : articles,
        'target' : target
    }
    return render(request, 'pages/articleResult.html', response)
#
# Views for finding car based on car's name
#
def findCar(request):
    #
    # Retrieve the search query
    #
    target = request.POST['carName']
    #
    # Retrieve all car objects in the database
    #
    cars = Car.objects.all()
    response = {
        'cars' : cars,
        'target' : target
    }
    return render(request, 'pages/carResult.html', response)
