from django.shortcuts import render
from django.shortcuts import redirect
from .models import Car, Transaction, Category, Article, Review
from . import forms

# Create your views here.
def home(request):
    return render(request,'pages/index.html',{})

def about(request):
    return render(request,'pages/about.html',{})

## masih bingung cara filter the certain article yg usernya mau
def articles(request):
    article = Article.objects.filter() 
    response = {'article': Article}
    return render(request,'pages/articles.html', response)

def cars(request):
    cars = Car.objects.all()
    response = {'cars' : Car}
    return render(request, 'pages/cars.html', response)

## masih bingung cara filter the certain car yg usernya mau
def carsView(request):
    car = Car.objects.filter() 
    response = {'car': Car}
    return render(request,'pages/cars.html', response)

def rentForm(request):
    if request.method == 'POST':
        form = forms.RentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.RentForm()
    return render(request, 'pages/rentForm.html', {'form': form})