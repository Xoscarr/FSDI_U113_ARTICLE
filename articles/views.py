from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView, 
    DeleteView,


)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    template_name = "article/list.html"
    model = Article


class ArticleDetailView(DetailView):
    template_name = "article/detail.html"
    model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/new.html"
    model = Article
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "article/edit.html"
    model = Article
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "article/delete.html"
    model = Article
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

