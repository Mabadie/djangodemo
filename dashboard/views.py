from decouple import config
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache


# Create your views here.
def dashboard_view(request):
    clicked = _get_clicked()
    decouple_test = config("TEST_DECOUPLE")
    return render(request, 'dashboard.html', {'clicked': clicked, 'decouple': decouple_test})


def update_clicked(request):
    clicked = _get_clicked() + 1
    cache.set('clicked', clicked)
    decouple_test = config("TEST_DECOUPLE")
    return render(request, 'dashboard.html', {'clicked': clicked, 'decouple': decouple_test})


def _get_clicked():
    clicked = cache.get('clicked')
    if clicked:
        clicked = clicked
    else:
        clicked = 0
    return clicked