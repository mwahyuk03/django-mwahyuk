from rest_framework import serializers
from ..models import Post

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=get_user_model()
#         fields = ['username']

class ReferencesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'description', 'link', 'author']
