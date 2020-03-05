from django.contrib import admin
from .models import *
# Register your models here.

#
# Register 5 models : Car, Transaction, Category, Article, Review
#
admin.site.register(Car)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Review)
