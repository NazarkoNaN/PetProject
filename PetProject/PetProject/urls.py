from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('demo.urls')),
    path('admin/', admin.site.urls),
    path('rest/', include('api.urls')),
]
