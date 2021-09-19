from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.urls import reverse

from .models import  subject

# Create your views here.

def index(request):
    return render(request,"index.html",  {}
    ) 


def course(request):
    return render(request,"course.html",{  
        "subjects" : subject.objects.all()
    })

def course_subject(request, subject_id):
    Subject = subject.objects.get(pk=subject_id)
    return render(request,"subject.html",{
        'subject' : Subject,
        'students' : Subject.students.all(),
        #'non_student' : student.objects.exclude(subjects=Subject).all()

    })





def writemessage(request):
    return render(request,"writemessage.html")


def result(request):
    name = request.POST['name']
    return render(request,"result.html",{'name': name})

def loginPage(request):
    return render(request,'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            return HttpResponse("มั่ว")    

    else:
        return render(request,"index.html")     

def logoutAcc(request):
    auth.logout(request)
    return redirect("/")

def registered(request, subject_id):
    if not request.user.is_authenticated :
        return render(request,"login.html")

    Subject = get_object_or_404(subject, pk = subject_id)  
    if request.user not in subject.students.all():
        subject.students.add(request.user)
       
        return redirect('/')