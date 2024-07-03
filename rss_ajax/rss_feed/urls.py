from django.urls import path
from . import views

urlpatterns = [
    path('fetch_rss/', views.fetch_rss, name='fetch_rss'),
    path('', views.index, name='index'),
]