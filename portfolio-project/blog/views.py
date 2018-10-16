from django.shortcuts import render

# Create your views here.

from .models import Blog


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})
