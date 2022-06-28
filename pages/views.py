from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'pages/pages.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/page_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'pages/page_form.html'
    fields = ['image', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)