from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.

from .models import *

def Admin(request):
    return render(request,"Admin.html",context = {"current_tab" : "Admin"})
def Students(request):
    return render(request,"Student.html",context = {"current_tab" : "Students"})

# def save_student(request):
#     Student_name = request.POST['Student_name']    
#     return render(request,"welcome.html",context={'Student_name':Student_name})

def Students_tab(request) :
    Students = Student.objects.all()
    return render(request , "Student.html", context = {"current_tab" : "Student",
                                                       "Students" : Students})

def save_student(request):
    student_item = Student(Student_name = request.POST['Student_name'],
                           register_id = request.POST['register_id'],
                           Student_contact = request.POST['Student_contact'],
   
                           active = True
                            )
    student_item.save()
    return redirect('/students')

def Books(request):
     return render(request,"Books.html",context = {"current_tab" : "Books"})

def Returns(request):
     return render(request,"Returns.html",context = {"current_tab" : "Returns"})