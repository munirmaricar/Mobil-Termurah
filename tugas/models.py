from django.db import models

# Create your models here.

#
# There are 5 models : Car, Transaction, Category, Article, Review
#
class Car(models.Model):
    carName = models.CharField(max_length=30)
    carCategory = models.CharField(max_length=20)
    carYear = models.CharField(max_length=4)
    carCity = models.CharField(max_length=50)
    carPrice = models.CharField(max_length=15)
    carDescription = models.CharField(max_length=1000)
class Transaction(models.Model):
    carName = models.ForeignKey(Car, on_delete=models.CASCADE)
class Category(models.Model):
    carCategory = models.ForeignKey(Car, on_delete=models.CASCADE)
    categoryName = models.CharField(max_length=20)
class Article(models.Model):
    carName = models.ForeignKey(Car, on_delete=models.CASCADE)
class Review(models.Model):
    carName = models.ForeignKey(Car, on_delete=models.CASCADE)
    carReview = models.CharField(max_length=1000)
