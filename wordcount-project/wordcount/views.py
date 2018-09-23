from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {"football": "the best"})


def barcelona(request):
    return HttpResponse("<h1>Forca Barca<h1>")
