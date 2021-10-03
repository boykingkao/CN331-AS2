from django.contrib.auth import logout
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Subject
# Create your tests here.

class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="user1", password= make_password('somepass@123'), email="user1@example.com")

        #subject = Subject.objects.create(subject_code = "CN191", subject_name = "Computer django", subject_semester  = 2, subject_year = 3,
        #subject_seat = 3, count = 0, status = open )
    
    def test_index_view_with_authenticate(self):
        '''index view'''
        c = Client()
        user = User.objects.get(username="user1")
        c.force_login(user)
        response = c.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    
    def test_index_view_without_authenticate(self):
        '''index view'''
        c = Client()
        user = User.objects.get(username="user1")  
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    
    def test_login_view_successful(self):
        '''logged in succe'''
        c = Client()
        user = User.objects.get(username="user1")  
        c.force_login
        response = c.post(reverse('login'),{'username' : 'user1', 'password' : "somepass@123"})
        self.assertEqual(response.status_code, 302)



    def test_login_view_unsuccessful(self):
        '''if not logged in it will back to login page with alert message'''
        c = Client()
        user = User.objects.get(username="user1")  
        response = c.post(reverse('login'),{'username' : 'user1', 'password' : ""})
        self.assertEqual(response.status_code, 302)

       

        

    #def test_course_subject(self):
        
    def test_course_page(self):
        c = Client()
        response = c.get(reverse('course'))
        self.assertEqual(response.status_code, 200)
    

    #ยังไม่เสร็จ
    def test_logout_Acc(self):
        '''logout page view'''
        c = Client()
        user = User.objects.get(username="user1")  
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code , 302)
    


    #ยังไม่เสร็จ
    def test_registered_not_logged_in(self):
        '''still not logged in'''
        c = Client()
        user = User.objects.get(username = "user1") 

        response = c.get('/loginPage/')
        self.assertEqual(response.status_code, 200)
        
    
    #def test_remove(self):
        
    
  

    

   
