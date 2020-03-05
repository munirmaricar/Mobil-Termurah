from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('cars', views.cars, name='cars'),
    path('carsView', views.carsView, name='carsView'),
    path('about', views.about, name='about'),
    path('articles', views.articles, name='articles')
]
