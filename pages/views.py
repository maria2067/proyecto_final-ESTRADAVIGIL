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
    paginate_by = 4
   
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/page_detail.html'
    context_object_name = 'post'



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'pages/page_form.html'
    fields = ['image', 'title', 'content']
    extra_context = {'creando': True, 'title':'Create post'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'pages/page_form.html'
    fields = ['image', 'title', 'content']
    extra_context = {'actualizando': True, 'title':'Update post'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'pages/page_confirm_delete.html'
    success_url = '/'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


