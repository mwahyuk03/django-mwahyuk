from django.urls import path 
from . import views

app_name = 'references'

urlpatterns = [
    path('postsref/', views.ReferencesListView.as_view(), name='api_postref_list'),
    path('postsref/<int:pk>/', views.ReferencesDetailView.as_view(), name='api_postref_detail'),
]