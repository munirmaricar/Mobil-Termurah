from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='index'),
    path('cars/',views.cars,name='cars'),
    path(r'CarsView/(?P<pk>\d+)/$',views.carsView,name='carsView'),
    path('findCar/', views.findCar, name='findCar'),
    path('RentForm/',views.rentForm,name='rentForm'),
    path('sendRentForm/', views.sendRentForm, name='sendRentForm'),
    path('articles/',views.articles,name='articles'),
    path('ArticleForm/',views.articleForm,name='articleForm'),
    path('SendArticleForm/', views.sendArticleForm, name='SendArticleForm'),
    path('chooseArticle/', views.chooseArticle, name='chooseArticle'),
    path('about/',views.about,name='about'),
    path('searchByCategory/', views.searchByCategory, name='searchByCategory'),
    path(r'rentingForm/(?P<pk>\d+)/$',views.rentingForm,name='rentingForm'),
    path(r'sendRentingForm/(?P<pk>\d+)/$',views.sendRentingForm,name='sendRentingForm'),
    path('listOfTransaction/', views.transaction, name='listOfTransaction'),
    path(r'sendReviewForm/(?P<pk>\d+)/$',views.sendReviewForm,name='sendReviewForm')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
