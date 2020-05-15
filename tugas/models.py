from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

#
# There are 5 models : Car, Transaction, Category, Article, Review
#
class Category(models.Model):
    categoryName = models.CharField(max_length=20)

    def __str__(self):
        return self.categoryName

class Car(models.Model):
    carName = models.CharField(max_length=30)
    carCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    carYear = models.CharField(max_length=4)
    carCity = models.CharField(max_length=50)
    carPrice = models.CharField(max_length=15)
    carDescription = models.CharField(max_length=1000)
    carImage = models.ImageField(upload_to= 'media/')
    carRating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    favourite = models.ManyToManyField(User, related_name="favourite_car", blank=True)

    def __str__(self):
        return self.carName

class Transaction(models.Model):
    carName = models.ForeignKey(Car, on_delete=models.CASCADE)
    transactionDuration = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)])
    
class Article(models.Model):
    articleTitle = models.CharField(primary_key=True, max_length=60)
    articleContent = models.CharField(max_length=10000)
    articleRating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    totalRatings = models.PositiveIntegerField(default=0)
    sumOfRatings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.articleTitle

class Review(models.Model):
    carName = models.ForeignKey(Car, on_delete=models.CASCADE)
    carReview = models.CharField(max_length=1000)
    carRating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
