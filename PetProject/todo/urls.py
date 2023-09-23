from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="to-do"),
    path('tasks/', include('tasks.urls'))
]