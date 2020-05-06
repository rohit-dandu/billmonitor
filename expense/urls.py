from django.urls import path #Import the path function
from . import views #import local views

urlpatterns = [
    path('', views.index, name="index"),
]