from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def dashboard_view(request):
    return render(request, 'dashboard.html', {'clicked': 500})