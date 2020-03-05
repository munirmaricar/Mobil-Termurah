from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('findCar', views.findCar, name='findCar'),
    path('cars', views.cars, name='cars'),
    path('carsView', views.carsView, name='carsView'),
    path('articles', views.articles, name='articles'),
    path('chooseArticle', views.chooseArticle, name='chooseArticle'),
    path('rentForm', views.rentForm, name='rentForm'),
    path('sendRentForm', views.sendRentForm, name='sendRentForm'),
    path('about', views.about, name='about')
]
