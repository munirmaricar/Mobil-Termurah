from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('cars/',views.cars,name='cars'),
    path('CarsView/',views.carsView,name='carsView'),
    path('findCar/', views.findCar, name='findCar'),
    path('RentForm/',views.rentForm,name='rentForm'),
    path('sendRentForm/', views.sendRentForm, name='sendRentForm'),
    path('articles/',views.articles,name='articles'),
    path('chooseArticle/', views.chooseArticle, name='chooseArticle'),
    path('about/',views.about,name='about'),
]
