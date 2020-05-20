from django.urls import path #Import the path function
from . import views #import local views

urlpatterns = [
    path('', views.expense, name="expense"),
    path('add_item',views.BillView.as_view(),name='add expense'),
]