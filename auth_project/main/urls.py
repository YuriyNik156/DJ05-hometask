from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # корневая страница
    path('register/', views.register, name='register'),
]
