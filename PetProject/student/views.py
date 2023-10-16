from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegisterUserForm
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

'''
def register_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(RegisterUser.as_view())
'''

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'student/register.html'
    success_url = reverse_lazy('student_login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect(index)
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.user_login()
        if user:
            login(request, user)
            return redirect(index)
    return render(request,"student/login.html",{'form':form})

@login_required(login_url='student_login')
def logout_view(request):
    logout(request)
    return redirect('student_login')
