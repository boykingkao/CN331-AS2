from django.contrib.auth.signals import user_logged_in
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout, login
from django.contrib import messages
from django.urls import reverse

from .models import Subject

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect("/loginPage")
    else:
        return render(request,"index.html")
    


def course(request):
    return render(request,"course.html",{  
        "subjects" : Subject.objects.all()
    })

def course_subject(request, subject_id):
    Subjects = Subject.objects.get(pk=subject_id)
   
    return render(request,"subject.html",{
        "test" : {"goh", "za", "lol"},
        'subject' : Subjects,
        'students' : Subjects.students.all(),
        'count' : Subjects.students.count(),
        'seat_left' : Subjects.subject_seat - Subjects.students.count() ,
        
        #'non_student' : student.objects.exclude(subjects=Subject).all()

    })




def loginPage(request):
    return render(request,'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/course')
        
        else:
            messages.info(request,"Username หรือ Password ผิด กรุณากรอกใหม่")
            return redirect('/loginPage') 

    else:
        return render(request,"index.html")     

def logoutAcc(request):
    auth.logout(request)
    return redirect("/")

def registered(request, subject_id):
    if not request.user.is_authenticated :
        #messages.warning(request, "Please Login")
        #return HttpResponseRedirect(reverse("login")+f"?next={request.path}")
        messages.info(request,"โปรด Login ก่อนทำการลงทะเบียนรายวิชา")
        return redirect("/loginPage")

    subject = get_object_or_404(Subject, pk = subject_id)  
    if request.user not in subject.students.all():
        subject.students.add(request.user)
       
        return redirect('/course')


def remove(request, subject_id):
    if not request.user.is_authenticated :
        #messages.warning(request, "Please Login")
        #return HttpResponseRedirect(reverse("login")+f"?next={request.path}")
        messages.info(request,"โปรด Login ก่อนทำการถอนรายวิชา")
        return redirect("/loginPage")

    subject = get_object_or_404(Subject, pk = subject_id)  
    if request.user in subject.students.all():
        subject.students.remove(request.user)       
        return redirect('/course')



