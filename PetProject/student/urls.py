from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='student'),
    path('login/', login, name='student_login'),
    path('register/', register, name='student_register'),
]