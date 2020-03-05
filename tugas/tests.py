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

    def testCarsViewPageURL(self):
        response = Client().get('/CarsView/')
        self.assertEqual(response.status_code, 200)

    def testFindCarPageURL(self):
        response = Client().get('/findCar/')
        self.assertEqual(response.status_code, 200)

    def testRentFormPageURL(self):
            response = Client().get('/RentForm/')
            self.assertEqual(response.status_code, 200)

    def testSendRentFormPageURL(self):
        response = Client().get('/sendRentForm/')
        self.assertEqual(response.status_code, 200)

    def testArticlesPageURL(self):
        response = Client().get('/articles/')
        self.assertEqual(response.status_code, 200)

    def testChooseArticlePageURL(self):
        response = Client().get('/chooseArticle/')
        self.assertEqual(response.status_code, 200)  

    def testAboutPageURL(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

#------------------------------------------------------------------------------ TEMPLATE TESTING -------------------------------------------------------------------------
    
    def testHomePageUsingTemplate(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'pages/index.html')

    def testCarsPageUsingTemplate(self):
        response = Client().get('/cars/')
        self.assertTemplateUsed(response, 'pages/cars.html')

    def testCarsViewPageUsingTemplate(self):
        response = Client().get('/CarsView/')
        self.assertTemplateUsed(response, 'pages/carsView.html')

    def testFindCarPageUsingTemplate(self):
        response = Client().get('/findCar/')
        self.assertTemplateUsed(response, 'pages/findCar.html')

    def testRentFormPageUsingTemplate(self):
        response = Client().get('/RentForm/')
        self.assertTemplateUsed(response, 'pages/rentForm.html')

    def testSendRentFormPageUsingTemplate(self):
        response = Client().get('/sendRentForm/')
        self.assertTemplateUsed(response, 'pages/sendRentForm.html')

    def testArticlesPageUsingTemplate(self):
        response = Client().get('/articles/')
        self.assertTemplateUsed(response, 'pages/articles.html')

    def testChooseArticlePageUsingTemplate(self):
        response = Client().get('/chooseArticle/')
        self.assertTemplateUsed(response, 'pages/chooseArticle.html')

    def testAboutPageUsingTemplate(self):
        response = Client().get('/about/')
        self.assertTemplateUsed(response, 'pages/about.html')

    # def testStoryUsingHomeFunction(self):
    #     found = resolve('/story6/')
    #     self.assertEqual(found.func, home)

    # def testContainsGreeting(self):
    #     response = Client().get('/story6/')
    #     response_content = response.content.decode('utf-8')
    #     self.assertIn("Hello, how are you?", response_content)

    # def testApps(self):
    #     self.assertEqual(Story6Config.name, 'story6')
    #     self.assertEqual(apps.get_app_config('story6').name, 'story6')
    
    # def testModelCreateNewStatus(self): 
    #     newStatus = Status.objects.create(name='Munir', status='Happy')
    #     countsAllNewStatus = Status.objects.all().count()
    #     self.assertEqual(countsAllNewStatus, 1)
    
    # def testModelReturnsStatusAttributes(self):
    #     newStatus = Status.objects.create(name='Munir', status='Happy')
    #     self.assertEqual(str(newStatus.name), newStatus.name)
    #     self.assertEqual(str(newStatus.status), newStatus.status)

    # def testStatusFormSoNotBlank(self):
    #     newStatus = StatusForm({'name':'', 'status':''})
    #     self.assertFalse(newStatus.is_valid())

    # def testModelReturnsStatus(self):
    #     newStatus = Status.objects.create(name='Munir', status='Happy')
    #     self.assertEqual(str(newStatus), newStatus.status)
