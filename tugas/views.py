from django.shortcuts import render, redirect
from django.http import HttpResponse
#
# Import all models
#
from .models import *

# Create your views here.

#
# View for index.html
#
def home(request):
    return render(request,'pages/index.html')
#
# View for finding car based on car's name
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
    carTarget = filter(lambda car: car.carName.lower() == target.lower(), cars)
    response = {
        'cars' : carTarget,
        'target' : target
    }
    return render(request, 'pages/carResult.html', response)
#
# View for cars.html
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
# View for carsView.html
#
def carsView(request):
    return render(request, 'pages/carsView.html')
#
# View for articles.html
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
# View for choosing article
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
# View for rentForm.html
#
def rentForm(request):
    return render(request, 'pages/rentForm.html')
#
# View for creating rent
#
def sendRentForm(request):
    # Check for POST request
    if(request.method == 'POST'):
        # Retrieve the values of POST parameters
        name = request.POST['carName']
        category = request.POST['carCategory']
        _categories = Category.objects.all()
        for _category in _categories:
            if category == _category.categoryName:
                category = _category
        year = request.POST['carYear']
        city = request.POST['carCity']
        price = request.POST['carPrice']
        description = request.POST['carDescription']
        # Save the comment to the database
        result = Car.objects.create(carName=name,carCategory=category,carYear=year,carCity=city,carPrice=price,carDescription=description)
        result.save()
        # Redirect to the index.html page to see the result
        return redirect('cars')
#
# View for about.html
#
def about(request):
    return render(request, 'pages/about.html')
