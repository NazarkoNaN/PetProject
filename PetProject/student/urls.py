from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='student'),
    path('login/', login_view, name='student_login'),
    path('logout', logout_view, name='student_logout'),
    path('register/', RegisterUser.as_view(), name='student_register'),
]