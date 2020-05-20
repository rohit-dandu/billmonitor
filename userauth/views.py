from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register_view(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, 'register.html', {"form":form})

# def login_view(request):
#     next = request.GET.get('next')
#     form = UserLoginForm(request)