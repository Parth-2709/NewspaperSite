from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Article, Comment

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body', )
    template_name = 'article_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(UserPassesTestMixin ,LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('comment',) 

    def form_valid(self, form):
        form.instance.author = self.request.user
        article = Article.objects.filter(pk=self.kwargs.get('pk'))
        form.instance.article = get_object_or_404(article)
        return super(CommentCreateView, self).form_valid(form)
    
    

# Create your views here.
