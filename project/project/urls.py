"""gohproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from firstpage import views
app_name = "firstpage"

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name = 'index' ),
    path('loginPage/',views.loginPage),
    path('loginPage/login',views.login, name= 'login'),
    
    path("logout",views.logoutAcc, name="logout"),
    
    path('course/',views.course, name ='course'), 
    path('course/<int:subject_id>', views.course_subject, name = 'subject'),  
    path('course/<int:subject_id>/regis', views.registered, name= 'register'), 
    path('course/<int:subject_id>/remove', views.remove, name= 'remove'),   
    
   

    ##################



    
]
 