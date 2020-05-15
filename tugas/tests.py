from django.test import TestCase, Client, LiveServerTestCase
from django.urls import resolve, reverse
from django.apps import apps
from .apps import *
from .views import *
from .models import *
from .forms import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# -------------------------------------------------------------------------------- URL TESTING ----------------------------------------------------------------------------
class UnitTesting (TestCase):

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

    # ------------------------------------------------------------------------------ TEMPLATE TESTING -------------------------------------------------------------------------

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

    # ------------------------------------------------------------------------------ FUNCTION TESTING -------------------------------------------------------------------------

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

    # -------------------------------------------------------------------------------- APP TESTING ----------------------------------------------------------------------------

    def testApplication(self):
        self.assertEqual(TugasConfig.name, 'tugas')
        self.assertEqual(apps.get_app_config('tugas').name, 'tugas')

    # ------------------------------------------------------------------------------ CONTENT TESTING --------------------------------------------------------------------------

    def testHomePageContainsPreviousText(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Previous", response_content)

    def testHomePageContainsNextButton(self):
        response = Client().get('/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Next", response_content)

    def testHomePageContainsElement(self):
        response = Client().get('/about/')
        response_content = response.content.decode('utf-8')
        self.assertIn("About", response_content)

    def testCarsPageContainsElement(self):
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Categories", response_content)

    # ------------------------------------------------------------------------------ MODEL TESTING --------------------------------------------------------------------------

    def testModelCreateNewCategory(self): 
        newCategory = Category.objects.create(categoryName='Sporty')
        numberOfCategories = Category.objects.all().count()
        self.assertEqual(numberOfCategories, 1)

    def testModelCreateNewCar(self): 
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png')
        numberOfCars= Category.objects.all().count()
        self.assertEqual(numberOfCars, 1)

    def testModelCreateNewArticle(self): 
        newArticle = Article.objects.create(articleTitle='Rising Demand of Electric Vehicles', articleContent='This is because of environmental concerns')
        numberOfArticles = Article.objects.all().count()
        self.assertEqual(numberOfArticles, 1)

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

class FunctionalTesting(LiveServerTestCase):
    def setUp(self):
        super().setUp()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1480')
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')

    def tearDown(self):
        self.driver.quit()
        super().tearDown()

    def testIfArticleReviewsAreUpdatedSynchronously(self):
        self.driver.get('http://127.0.0.1:8000/articles/')
        self.driver.find_element_by_id("submitAnArticle").click()
        time.sleep(5)
        self.driver.find_element_by_id("articleTitle").send_keys("BMW")
        time.sleep(1)
        self.driver.find_element_by_id("articleContent").send_keys("They are a manufacturer that produces cars.")
        time.sleep(1)
        self.driver.find_element_by_id("submitArticle").click()
        time.sleep(5)
        self.driver.find_element_by_id("seeArticleBMW").click()
        time.sleep(5)
        self.assertEqual("No Rating", self.driver.find_element_by_id("articleRating").text)
        self.driver.find_element_by_id("ratings").click()
        self.driver.find_element_by_id("five").click()
        self.driver.find_element_by_name("submitRatingButton").click()
        time.sleep(5)
        self.driver.find_element_by_id("ratings").click()
        self.driver.find_element_by_id("one").click()
        self.driver.find_element_by_name("submitRatingButton").click()        
        time.sleep(5)
        self.assertEqual("3", self.driver.find_element_by_id("articleRating").text)

        





