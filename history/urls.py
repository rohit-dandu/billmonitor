from django.urls import path #Import the path function
from . import views #import local views

urlpatterns = [
    path('history/<int:pk>', views.HistoryView.as_view(), name='show-history'),
    path('', views.HistoryList.as_view(), name="history"),
]