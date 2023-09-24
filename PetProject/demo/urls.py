from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('to-do/', include('todo.urls'), name="to-do"),
    path('student/', include('student.urls'), name="student"),
]