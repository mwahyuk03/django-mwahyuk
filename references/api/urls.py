from django.urls import path 
from . import views

app_name = 'references'

urlpatterns = [
    path('refpost/', views.ReferencesListView.as_view(), name='api_postref_list'),
    path('refpost/<int:pk>/', views.ReferencesDetailView.as_view(), name='api_postref_detail'),
]