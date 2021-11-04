from django.contrib import admin
from django.urls import path
from qrcode_generator import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('send', views.home),
]