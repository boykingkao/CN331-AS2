

from django.urls import path
from .views import index
from . import views


app_name = "firstpage"

urlpatterns = [
    path('',index),
    
    
]
