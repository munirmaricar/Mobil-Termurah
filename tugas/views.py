from django.shortcuts import render,redirect

# Create your views here.

#
# Views for index.html
#
def home(request):
    return render(request,'pages/index.html',{})
#
# Views for cars.html
#
def cars(request):
    return render(request, 'pages/cars.html')
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
