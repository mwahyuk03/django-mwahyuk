from django import template 
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag()
def total_posts():
    return Post.objects.count()
    
@register.inclusion_tag('references/post/latest_ref.html')
def show_latest_ref(count=5):
    latest_ref = Post.objects.order_by('-created')[:count]
    return {'latest_ref': latest_ref}

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))