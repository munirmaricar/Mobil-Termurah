from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
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
    category = Category.objects.all()
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
        'categories' : category,
    }
    return render(request, 'pages/carResult.html', response)
#
# View for cars.html
#
def cars(request):
    #
    # Retrieve all car objects in the table
    #
    cars = Car.objects.all()
    #
    # Assign the rating in each car
    #
    for car in cars:
        review = list(filter(lambda review : review.carName == car, Review.objects.all()))
        ratings = list(map(lambda review : review.carRating, review))
        car.carRating = int(sum(ratings)/len(review)) if len(review) > 0 else 0
    response = {
        'cars' : cars,
    }
    return render(request, 'pages/cars.html', response)
#
# View for carsView.html
#
def carsView(request, pk):
    car = Car.objects.get(id=pk)
    review = list(filter(lambda review : review.carName == car, Review.objects.all()))
    ratings = list(map(lambda review : review.carRating, review))
    rating = int(sum(ratings)/len(review)) if len(review) > 0 else 0
    print(rating)

    is_favourite = False
    if car.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    response = {'car' : car , 'reviews' : review, 'rating' : rating, 'is_favourite' : is_favourite}
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
        image = request.FILES['carImage']
        # Save the comment to the database
        result = Car.objects.create(carName=name,carCategory=category,carYear=year,carCity=city,carPrice=price,carDescription=description, carImage=image)
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
#
# View for renting a car
#
def rentingForm(request, pk):
    car = Car.objects.get(id=pk)
    response = {
        'car' : car
    }
    return render(request, 'pages/rentingForm.html', response)
#
# View for transaction when renting a car
#
def sendRentingForm(request, pk):
    car = Car.objects.get(id=pk)
    #
    # Retrieve all the duration query
    #
    duration = request.POST['transactionDuration']
    #
    # Save the request to the database
    #
    result = Transaction.objects.create(carName=car, transactionDuration=duration)
    result.save()
    #
    # Redirect the page to listOfTransaction.html
    #
    return redirect('listOfTransaction')
#
# View for list of transaction
#
def transaction(request):
    transactions = Transaction.objects.all()
    response = {
        'transactions' : transactions
    }
    return render(request, 'pages/listOfTransaction.html', response)
#
# View for sending a review
#
def sendReviewForm(request, pk):
    #
    # Retrieve all the queries
    #
    car = Car.objects.get(id=pk)
    review = request.POST['carReview']
    rating = request.POST['carRating']
    #
    # Save the queries
    #
    result = Review.objects.create(carName=car, carReview=review, carRating=rating)
    result.save()
    #
    # Redirect to cars.html
    #
    return redirect('cars')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'pages/register.html',{'form' : form})
    
def favouriteCar(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
        if car.favourite.filter(id=request.user.id).exists():
            car.favourite.remove(request.user)
        else:
            car.favourite.add(request.user)
    return redirect('favoriteCarsPage')

def favoriteCarsPage(request):
    cars = Car.objects.all()
    for car in cars:
        review = list(filter(lambda review : review.carName == car, Review.objects.all()))
        ratings = list(map(lambda review : review.carRating, review))
        car.carRating = int(sum(ratings)/len(review)) if len(review) > 0 else 0
    response = {
        'cars' : cars,
    }
    return render(request, 'pages/favoriteCarsPage.html', response)