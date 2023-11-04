"""Module providing a views."""
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post, Category
from .forms import PostForm, EditForm


class HomeView(ListView):
    '''
        Class name
    '''
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    '''
        Class name
    '''
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    '''
        Class name
    '''
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    '''
        Class name
    '''
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    '''
        Class name
    '''
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','author','body']


class DeletePostView(DeleteView):
    '''
        Class name
    '''
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def category_view(request,cats):
    '''
        def name
    '''
    category_posts = Post.objects.filter(category=cats)
    return render(request,'categories.html', {'cats':cats, 'category_posts' : category_posts} )
