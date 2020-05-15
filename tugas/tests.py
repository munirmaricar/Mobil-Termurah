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
from selenium.webdriver.common.keys import Keys
import time

# -------------------------------------------------------------------------------- URL TESTING ----------------------------------------------------------------------------
class tests (TestCase):

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

    def testRegisterURL(self):
        response = Client().get('/register/')
        self.assertEqual(response.status_code,200)

    def testSeeFavoriteCarPage(self):
        response = response = Client().get('/favoriteCarsPage')
        self.assertEqual(response.status_code,301)

    def testFavoriteThisCar(self):
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png')
        url = reverse('favouriteCar', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

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

    def testRegisterURL(self):
        response = Client().get('/register/')
        self.assertTemplateUsed(response, 'pages/register.html')

    def testSeeFavoriteCarPageTemplate(self):
        response = Client().get('/favoriteCarsPage/')
        self.assertTemplateUsed(response, 'pages/favoriteCarsPage.html')

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

    def testFavoriteCarPageFunction(self):
        found = resolve('/favoriteCarsPage/')
        self.assertEqual(found.func, favoriteCarsPage)

    def testFavoriteThisCarFunction(self):
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png')
        found = resolve('/favouriteCar/(?P<1>\d+)/$')
        self.assertEqual(found.func, favouriteCar)

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

    def testModelFavoriteThisCar(self): 
        newUser = User.objects.create_user('groupk3', 'groupk3@mail.com', 'password')
        newUser.last_name = 'ppw'
        newUser.save()
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png',carRating='4')
        newCar.favourite.add(newUser)
        self.assertEqual(newCar.favourite.get(id=newUser.id), newUser)
        newCar.favourite.remove(newUser)
        self.assertEqual(newCar.favourite.all().count(), 0)
        response = Client().get('/cars/')
        response_content = response.content.decode('utf-8')
        self.assertIn("4", response_content)
        response = Client().get('/favoriteCarsPage/')
        response_content = response.content.decode('utf-8')
        self.assertIn("4", response_content)

class GAFunctionalTest(LiveServerTestCase):
    def setUp(self):
        newUser = User.objects.create_user('groupk3', 'groupk3@mail.com', 'password')
        newUser.last_name = 'ppw'
        newUser.save()
        newCategory = Category.objects.create(categoryName='Luxury')
        newCar = Car.objects.create(carName='Alphard', carCategory=newCategory, carYear='2020', carCity='Jakarta', carPrice='Rp. 1,000,000,000', carDescription='Spacious Luxury Vehicle', carImage='static/img/Car.png',carRating='4')
        super().setUp()
        chrome_options = webdriver.ChromeOptions()
        # self.driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1480')
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')

    def tearDown(self):
        self.driver.quit()
        super().tearDown()

    def testRegisterThenLogInThenFavoriteThisCarThenUnfavoriteThisCar(self):
        self.driver.get(self.live_server_url)
        response_page = self.driver.page_source

        time.sleep(5)
        self.driver.find_element_by_name('Register').click()
        time.sleep(2)

        self.driver.find_element_by_name('username').send_keys('groupk3account')
        self.driver.find_element_by_name('first_name').send_keys('group')
        self.driver.find_element_by_name('last_name').send_keys('k3ppw')
        self.driver.find_element_by_name('email').send_keys('groupk3mail@mail.com')
        self.driver.find_element_by_name('password1').send_keys('password123')
        self.driver.find_element_by_name('password2').send_keys('password123')
        time.sleep(2)
        self.driver.find_element_by_name('RegisterButton').click()

        self.driver.find_element_by_name('username').send_keys('groupk3account')
        self.driver.find_element_by_name('first_name').send_keys('group')
        self.driver.find_element_by_name('last_name').send_keys('k3ppw')
        self.driver.find_element_by_name('email').send_keys('groupk3mail@mail.com')
        self.driver.find_element_by_name('password1').send_keys('123Adadeh')
        self.driver.find_element_by_name('password2').send_keys('123Adadeh')
        time.sleep(2)
        self.driver.find_element_by_name('RegisterButton').click()

        time.sleep(5)
        self.driver.find_element_by_name('LogIn').click()
        time.sleep(5)

        self.driver.find_element_by_name('username').send_keys('groupk3')
        self.driver.find_element_by_name('password').send_keys('password')
        time.sleep(3)
        self.driver.find_element_by_name('loginbutton').click()
        time.sleep(2)

        self.driver.find_element_by_name('rentacarnow').click()
        car = self.driver.find_elements_by_name('carname')
        car[0].click()
        time.sleep(2)
        self.driver.find_element_by_name('favthiscar').click()
        time.sleep(2)

        response_page = self.driver.page_source
        carname = self.driver.find_elements_by_id('carname')
        self.assertIn('ALPHARD', carname[0].text)

        time.sleep(2)
        self.driver.find_element_by_name('remove').click()
        time.sleep(2)
        response_page = self.driver.page_source
        self.assertIn('You have no favourite car.', response_page)

    def testFindCarWithSearchBar(self):
        self.driver.get(self.live_server_url)
        response_page = self.driver.page_source

        time.sleep(5)
        carname = 'Alphard'
        for char in carname:
            self.driver.find_element_by_name('carName').send_keys(char)
            time.sleep(1)
        self.driver.find_element_by_name('carName').send_keys(Keys.RETURN)
        time.sleep(5)

        response_page = self.driver.page_source
        time.sleep(5)
        carname = self.driver.find_elements_by_id('carname')
        self.assertIn('ALPHARD', carname[0].text)

    def testSubmitAnArticleThenSeeArticle(self):
        self.driver.get(self.live_server_url)
        response_page = self.driver.page_source

        time.sleep(5)
        self.driver.find_element_by_name('Article').click()
        time.sleep(2)

        self.driver.find_element_by_name('submitarticlebtn').click()

        self.driver.find_element_by_name('articleTitle').send_keys('MobilTermurah Article')
        self.driver.find_element_by_name('articleContent').send_keys('We have various cars for rent')
        time.sleep(2)
        self.driver.find_element_by_name('submitarticle').click()

        response_page = self.driver.page_source
        time.sleep(2)
        articleTitle = self.driver.find_elements_by_id('articleTitle')
        self.assertIn('MobilTermurah Article', articleTitle[0].text)

        self.driver.find_element_by_name('articleTitle').click()
        response_page = self.driver.page_source
        self.assertIn('We have various cars for rent', response_page)

    def testRentYourCarNow(self):
        self.driver.get(self.live_server_url)
        response_page = self.driver.page_source

        time.sleep(5)
        self.driver.find_element_by_name('rentyourcar').click()
        time.sleep(2)

        self.driver.find_element_by_id('nameinput').send_keys('Mercedez Benz')
        self.driver.find_element_by_name('carCategory').click()
        self.driver.find_element_by_name('categoryopt').click()
        self.driver.find_element_by_name('carYear').send_keys('2020')
        self.driver.find_element_by_name('carCity').send_keys('Jakarta')
        self.driver.find_element_by_name('carDescription').send_keys('A car')
        self.driver.find_element_by_name('carPrice').send_keys('600000')
        self.driver.find_element_by_name('carImage').send_keys('static/img/car.png')
        time.sleep(2)
        self.driver.find_element_by_name('rentmycar').click()

        carname = self.driver.find_elements_by_name('carname')
        time.sleep(2)
        self.assertIn('Sienta', carname)