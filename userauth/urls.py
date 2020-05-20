from django.urls import path #Import the path function
from . import views #import local views

urlpatterns = [
    path('register/', views.register_view, name="register_view"),
    # path('login/', views.login_view, name="login_veiw")
]