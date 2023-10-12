from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='student'),
    path('login/', view_login, name='student_login'),
    path('logout', view_logout, name='student_logout'),
    path('register/', RegisterUser.as_view(), name='student_register'),
]