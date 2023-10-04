from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import StudentModelForm, StudentCreationForm
from .models import Student


def index(request):
    return render(request,'student/index.html', {'form':form})

def login(request):
    return render(request,'student/login.html')

def register(request):
    form = StudentCreationForm(request.POST or None)

    if form.is_valid():
        user = User(username=form.firstname,
                    last_name=form.lastname,
                    email=form.email,
                    password=form.password1)
        user.save()
        student = Student(user=user, phonenumber=form.phone)
        student.save()
        return render(request, 'student/index.html')

    return render(request,'student/register.html', {"form":form})
