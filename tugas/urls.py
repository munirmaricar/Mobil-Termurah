from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('/about',views.about,name='about'),
    path('/articles',views.articles,name='articles'),
    path('/cars',views.cars,name='cars'),
    path('/CarsView',views.carsView,name='carsView'),
    path('/RentForm',views.rentForm,name='rentForm'),
]