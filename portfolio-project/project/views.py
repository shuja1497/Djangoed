from django.shortcuts import render

# Create your views here.

from .models import Project


def home(request):
    projects = Project.objects  # getting all list of projects from the database
    return render(request, 'project/homepage.html', {'projects': projects})
