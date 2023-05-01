from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import *
from .filters import NewsFilter
from .forms import CreateNewsForm

class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'mainnews.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class Textnews(DetailView):
    model = Post
    template_name = 'textnews.html'
    context_object_name = 'post'


class CreateNews(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = CreateNewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categoryType= 'NW'
        return super().form_valid(form)


class UpdateNews(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = CreateNewsForm
    model = Post
    template_name = 'news_edit.html'


class DeleteNews(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'news_delete.html'
    success_url= reverse_lazy('News_list')

class ArticlesCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('news.add_post')
    form_class = CreateNewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categoryType= 'AR'
        return super().form_valid(form)


class UpdateArticles(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = CreateNewsForm
    model = Post
    template_name = 'news_edit.html'


class DeleteArticles(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('News_list')