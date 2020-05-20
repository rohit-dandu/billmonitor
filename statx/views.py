from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def statx(request):
    # return HttpResponse("<h1>BillMonitor!</h1>")
    return render(request, 'statx/stats.html')
    