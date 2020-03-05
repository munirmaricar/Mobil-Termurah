from django.test import TestCase, Client
from django.urls import resolve
from django.apps import apps
from .apps import *
from .views import *
from .models import *
from .forms import  

# Create your tests here.
class Story6UnitTest (TestCase):
    def testStoryURL(self):
        response = Client().get('/story6/')
        self.assertEqual(response.status_code, 200)

    def testStoryUsingTemplate(self):
        response = Client().get('/story6/')
        self.assertTemplateUsed(response, 'story.html')

    def testStoryUsingHomeFunction(self):
        found = resolve('/story6/')
        self.assertEqual(found.func, home)

    def testContainsGreeting(self):
        response = Client().get('/story6/')
        response_content = response.content.decode('utf-8')
        self.assertIn("Hello, how are you?", response_content)

    def testApps(self):
        self.assertEqual(Story6Config.name, 'story6')
        self.assertEqual(apps.get_app_config('story6').name, 'story6')
    
    def testModelCreateNewStatus(self): 
        newStatus = Status.objects.create(name='Munir', status='Happy')
        countsAllNewStatus = Status.objects.all().count()
        self.assertEqual(countsAllNewStatus, 1)
    
    def testModelReturnsStatusAttributes(self):
        newStatus = Status.objects.create(name='Munir', status='Happy')
        self.assertEqual(str(newStatus.name), newStatus.name)
        self.assertEqual(str(newStatus.status), newStatus.status)

    def testStatusFormSoNotBlank(self):
        newStatus = StatusForm({'name':'', 'status':''})
        self.assertFalse(newStatus.is_valid())

    def testModelReturnsStatus(self):
        newStatus = Status.objects.create(name='Munir', status='Happy')
        self.assertEqual(str(newStatus), newStatus.status)
