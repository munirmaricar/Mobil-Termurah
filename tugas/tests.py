from django.test import TestCase, Client
from django.urls import resolve
from django.apps import apps
from .apps import *
from .views import *
from .models import *
from .forms import *

class GroupAssignmentUnitTest (TestCase):

#-------------------------------------------------------------------------------- URL TESTING ----------------------------------------------------------------------------

    def testHomePageURL(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def testCarsPageURL(self):
        response = Client().get('/cars/')
        self.assertEqual(response.status_code, 200)

    def testRentFormPageURL(self):
            response = Client().get('/RentForm/')
            self.assertEqual(response.status_code, 200)

    def testArticlesPageURL(self):
        response = Client().get('/articles/')
        self.assertEqual(response.status_code, 200)

    def testArticleFormPageURL(self):
        response = Client().get('/ArticleForm/')
        self.assertEqual(response.status_code, 200)

    def testAboutPageURL(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def testTransactionsPageURL(self):
        response = Client().get('/listOfTransaction/')
        self.assertEqual(response.status_code, 200)

#------------------------------------------------------------------------------ TEMPLATE TESTING -------------------------------------------------------------------------
    
    def testHomePageUsingTemplate(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'pages/index.html')

    def testCarsPageUsingTemplate(self):
        response = Client().get('/cars/')
        self.assertTemplateUsed(response, 'pages/cars.html')

    def testRentFormPageUsingTemplate(self):
        response = Client().get('/RentForm/')
        self.assertTemplateUsed(response, 'pages/rentForm.html')

    def testArticlesPageUsingTemplate(self):
        response = Client().get('/articles/')
        self.assertTemplateUsed(response, 'pages/articles.html')

    def testArticleFormPageUsingTemplate(self):
        response = Client().get('/ArticleForm/')
        self.assertTemplateUsed(response, 'pages/articleForm.html')

    def testAboutPageUsingTemplate(self):
        response = Client().get('/about/')
        self.assertTemplateUsed(response, 'pages/about.html')

    def testTransactionsPageUsingTemplate(self):
        response = Client().get('/listOfTransaction/')
        self.assertTemplateUsed(response, 'pages/listOfTransaction.html')

#------------------------------------------------------------------------------ FUNCTION TESTING -------------------------------------------------------------------------

    def testHomePageUsingFunction(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def testCarsPageUsingFunction(self):
        found = resolve('/cars/')
        self.assertEqual(found.func, cars)

    def testFindCarPageUsingFunction(self):
        found = resolve('/findCar/')
        self.assertEqual(found.func, findCar)

    def testRentFormPageUsingFunction(self):
        found = resolve('/RentForm/')
        self.assertEqual(found.func, rentForm)

    def testSendRentFormPageUsingFunction(self):
        found = resolve('/sendRentForm/')
        self.assertEqual(found.func, sendRentForm)

    def testArticlesPageUsingFunction(self):
        found = resolve('/articles/')
        self.assertEqual(found.func, articles)

    def testArticleFormPageUsingFunction(self):
        found = resolve('/ArticleForm/')
        self.assertEqual(found.func, articleForm)        

    def testChooseArticlePageUsingFunction(self):
        found = resolve('/chooseArticle/')
        self.assertEqual(found.func, chooseArticle)

    def testAboutPageUsingFunction(self):
        found = resolve('/about/')
        self.assertEqual(found.func, about)

    def testSendArticleFormPageUsingFunction(self):
        found = resolve('/SendArticleForm/')
        self.assertEqual(found.func, sendArticleForm)

    def testSearchByCategoryPageUsingFunction(self):
        found = resolve('/searchByCategory/')
        self.assertEqual(found.func, searchByCategory)

    def testTransactionPageUsingFunction(self):
        found = resolve('/listOfTransaction/')
        self.assertEqual(found.func, transaction)

#-------------------------------------------------------------------------------- APP TESTING ----------------------------------------------------------------------------

    def testApplication(self):
        self.assertEqual(TugasConfig.name, 'tugas')
        self.assertEqual(apps.get_app_config('tugas').name, 'tugas')

#------------------------------------------------------------------------------ CONTENT TESTING --------------------------------------------------------------------------

    def testHomePageContainsHomeButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Home", response_content)

    def testHomePageContainsCarsButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Cars", response_content)
    
    def testHomePageContainsArticleButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Article", response_content)

    def testHomePageContainsAboutButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("About", response_content)

    def testHomePageContainsPreviousButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Previous", response_content)

    def testHomePageContainsNextButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Next", response_content)

    def testHomePageContainsRentACarButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Rent a Car Now!", response_content)

    def testHomePageContainsRentOutCarButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Rent Your Car Now!", response_content)

    def testCarsPageContainsCategories(self):
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Categories", response_content)

    def testCarsPageContainsSedanCategory(self):
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Sedan", response_content)

    def testCarsPageContainsHatchbackCategory(self):
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Hatchback", response_content)

    def testCarsPageContainsFamilyCarCategory(self):
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Family Car", response_content)

    def testCarsPageContainsLCGCCategory(self):
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("LCGC", response_content)

    def testCarsPageContainsJeepCategory(self):
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Jeep", response_content)

    def testCarsPageContainsTruckCategory(self):
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Truck", response_content)

    def testCarsPageContainsHomeButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Home", response_content)

    def testCarsPageContainsCarsButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Cars", response_content)
    
    def testCarsPageContainsArticleButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Article", response_content)

    def testCarsPageContainsAboutButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("About", response_content)

    def testCarsPageContainsSearchButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Search", response_content)

    def testArticlePageContainsHomeButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Home", response_content)

    def testArticlePageContainsCarsButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Cars", response_content)
    
    def testArticlePageContainsArticleButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Article", response_content)

    def testArticlePageContainsAboutButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("About", response_content)

    def testAboutPageContainsHomeButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Home", response_content)

    def testAboutPageContainsCarsButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Cars", response_content)
    
    def testAboutPageContainsArticleButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Article", response_content)

    def testAboutPageContainsAboutButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("About", response_content)
    
#------------------------------------------------------------------------------ MODEL TESTING --------------------------------------------------------------------------

    def testModelCreateNewCategory(self): 
        newCategory = Category.objects.create(categoryName='Sporty')
        numberOfCategories = Category.objects.all().count()
        self.assertEqual(numberOfCategories, 1)

    def testModelCreateNewCar(self): 
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png')
        numberOfCars= Category.objects.all().count()
        self.assertEqual(numberOfCars, 1)

    def testModelCreateNewTransaction(self): 
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png')
        newTransaction = Transaction.objects.create(carName=newCar)
        numberOfTransactions = Transaction.objects.all().count()
        self.assertEqual(numberOfTransactions, 1)

    def testModelCreateNewArticle(self): 
        newArticle = Article.objects.create(articleTitle='Rising Demand of Electric Vehicles', articleContent='This is because of environmental concerns')
        numberOfArticles = Article.objects.all().count()
        self.assertEqual(numberOfArticles, 1)

    def testModelCreateNewReview(self): 
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png')
        newReview = Review.objects.create(carName=newCar, carReview='Highly recommend this car to anybody who is rich!')
        numberOfReviews = Review.objects.all().count()
        self.assertEqual(numberOfReviews, 1)

    def testModelCategoryReturnsString(self):
        newCategory = Category.objects.create(categoryName='Sporty')
        self.assertEqual(str(newCategory), newCategory.categoryName)

    def testModelCarReturnsString(self):
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png')
        self.assertEqual(str(newCar), newCar.carName)

    def testModelArticleReturnsString(self):
        newArticle = Article.objects.create(articleTitle='Rising Demand of Electric Vehicles', articleContent='This is because of environmental concerns')
        self.assertEqual(str(newArticle), newArticle.articleTitle)
