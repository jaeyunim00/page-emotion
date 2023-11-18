# sentiment_analysis/urls.py

from django.urls import path
from .views import index, get_comments

urlpatterns = [
    path('', index, name='index'),
    path('get_comments/', get_comments, name='get_comments'),
]
