from django.shortcuts import render, redirect
from django.http import HttpResponse
#
# Import regex module for the search function
#
import re
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
    #
    # Create a regex pattern
    #
    pattern = re.compile(target, re.IGNORECASE)
    #
    # Use lambda to find the cars
    #
    carTarget = filter(lambda car: re.search(pattern, car.carName), cars)
    response = {
        'cars' : carTarget,
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
def carsView(request, pk):
    car = Car.objects.get(id=pk)
    review = list(filter(lambda review : review.carName.carName == car.carName, Review.objects.all()))
    ratings = list(map(lambda review : review.carRating, review))
    rating = int(sum(ratings)/len(review)) if len(review) > 0 else 0
    response = {'car' : car , 'reviews' : review, 'rating':rating,}
    return render(request, 'pages/carsView.html', response)
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
# View for sending an article
#
def sendArticleForm(request):
    #
    # Retrieve all the queries
    #
    title = request.POST['articleTitle']
    content = request.POST['articleContent']
    #
    # Save the request to the database
    #
    result = Article.objects.create(articleTitle=title,articleContent=content)
    result.save()
    #
    # Redirect to articles.html
    #
    return redirect('articles')
#
# View for choosing article
#
def chooseArticle(request):
    #
    # Retrieve the search query
    #
    target = request.POST['articleTitle']
    #
    # Retrieve all article object in the database
    #
    articles = Article.objects.all()
    #
    # Choose the article
    #
    for article in articles:
        if target == article.articleTitle:
            response = {
                'title' : article.articleTitle,
                'content' : article.articleContent
            }
    return render(request, 'pages/articleResult.html', response)
#
# View for rentForm.html
#
def rentForm(request):
    #
    # Retrieve all categories type in database
    #
    categories = Category.objects.all()
    #
    # Assign it to a variable for rendering
    #
    response = {
        'categories' : categories
    }
    return render(request, 'pages/rentForm.html', response)

#
# View to print article form
#
def articleForm(request):
    return render(request, 'pages/articleForm.html')
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
#
# View for finding all cars by category
#
def searchByCategory(request):
    #
    # Retrieve the category value from the checkbox
    #
    target = request.POST['vehicle']
    #
    # Retrieve all car objects in the database
    #
    cars = Car.objects.all()
    #
    # Use lambda to find the cars
    #
    carTarget = filter(lambda car: target==car.carCategory.categoryName, cars)
    response = {
        'cars' : carTarget,
    }
    return render(request, 'pages/carResult.html', response)
