from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import (SearchVector,SearchQuery,SearchRank)
#from .forms import SearchForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView


class ReferencesListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    context_object_name = 'postsref'
    paginate_by = 3
    template_name = 'references/post/list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        tag_slug = self.kwargs.get('tag_slug')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
class ReferencesCreateView(CreateView):
    model = Post
   # fields = ['title', 'slug', 'author', 'body', 'tags', 'status']
    fields = ['title', 'description', 'link']
    template_name = 'references/post/references_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title, allow_unicode=True)

        return super().form_valid(form)

class ReferencesUpdateView(UpdateView):
    model = Post
    #fields = ['title', 'slug', 'author', 'body', 'tags', 'status']
    fields = ['title', 'description', 'link']
    template_name = 'references/post/references_form.html'
    query_pk_and_slug = True

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title, allow_unicode=True)

        return super().form_valid(form)

class ReferencesDeleteView(DeleteView):
    model = Post
    template_name = 'references/post/references_confirm_delete.html'
    success_url = reverse_lazy('references:references_list')
    query_pk_and_slug = True

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.filter(author=self.request.user)
