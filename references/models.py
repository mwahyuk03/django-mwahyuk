from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish', blank=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'references_posts') 
    link = models.URLField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('references:references_list')
