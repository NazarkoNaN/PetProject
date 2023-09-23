from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='task_list'),
    path('update_task/<int:pk>/', updateTask, name='update_task'),
    path('delete_task/<int:pk>/', deleteTask, name='delete_task')
]