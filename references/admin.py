from django.contrib import admin
from .models import Post

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'author', 'link', 'publish')
    list_filter = ('created', 'publish', 'author')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title', 'description')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('author', 'publish')