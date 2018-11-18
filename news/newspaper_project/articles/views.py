from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
# Create your views here.


class ArticlesListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticlesDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticlesUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'


class ArticlesDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')



