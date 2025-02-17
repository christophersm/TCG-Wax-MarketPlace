from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tcg_pages.urls')),  # Include the urls of tcg_pages here
]
