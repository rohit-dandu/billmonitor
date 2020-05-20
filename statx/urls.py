from django.urls import path #Import the path function
from . import views #import local views

urlpatterns = [
    path('stats/', views.statx, name="statx"),
]