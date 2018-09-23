from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello')


def barcelona(request):
    return HttpResponse("<h1>Forca Barca<h1>")
