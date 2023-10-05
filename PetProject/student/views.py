from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import StudentModelForm, StudentCreationForm
from .models import Student


def index(request):
    return render(request,'student/index.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email, password=password)

        if user is not None:
            login(request,user)
            redirect('student')

    return render(request,'student/login.html')

def register(request):
    form = StudentCreationForm(request.POST or None)

    if form.is_valid():
        user = User(username=form.cleaned_data['firstname'],
                    last_name=form.cleaned_data['lastname'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'])
        student = Student(user=user,
                          phone=form.cleaned_data['phone'])

        user.save()
        student.save()
        return redirect('student')

    return render(request,'student/register.html', {"form":form})
