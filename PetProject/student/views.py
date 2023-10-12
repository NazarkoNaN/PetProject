from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import StudentModelForm, StudentCreationForm, LoginUserForm, RegisterUserForm
from .models import Student

@login_required(login_url='student_login')
def index(request):
    user = request.user
    print(user)
    username = user.username
    last_name = user.last_name
    email = user.email

    student = Student.objects.get(user=user.id)

    phone = student.phone
    course = student.course

    context = {'username':username,
               'last_name':last_name,
               'email':email,
               'phone':phone,
               'course':course
               }
    return render(request,'student/index.html', context)


# class LoginUser(LoginView):
#     form_class = LoginUserForm
#     template_name = 'student/login.html'
#
#     def get_success_url(self):
#         return reverse_lazy('student')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'student/register.html'
    success_url = reverse_lazy('student_login')


def view_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)
        user = authenticate(username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student')

    return render(request,'student/login.html')

@login_required(login_url='student_login')
def view_logout(request):
    logout(request)
    return redirect('student_login')


# def register(request):
#     if request.user.is_authenticated:
#         return redirect('student')
#
#     form = StudentCreationForm(request.POST or None)
#
#     if form.is_valid():
#         user = User(username=form.cleaned_data['firstname'],
#                     last_name=form.cleaned_data['lastname'],
#                     email=form.cleaned_data['email'],
#                     password=form.cleaned_data['password1'])
#         student = Student(user=user,
#                           phone=form.cleaned_data['phone'])
#
#         user.save()
#         student.save()
#
#         user = authenticate(request, id=user.id)
#
#         login(user)
#         return redirect('student')
#
#     return render(request,'student/register.html', {"form":form})

