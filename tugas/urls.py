from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='index'),
    path('findCar/', views.findCar, name='findCar'),
    path('chooseArticle/', views.chooseArticle, name='chooseArticle'),
    path('sendRentForm/', views.sendRentForm, name='sendRentForm'),
    path('about/',views.about,name='about'),
    path('articles/',views.articles,name='articles'),
    path('cars/',views.cars,name='cars'),
    path('CarsView/',views.carsView,name='carsView'),
    path('RentForm/',views.rentForm,name='rentForm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
