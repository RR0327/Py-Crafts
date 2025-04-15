from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/json/', views.download_json, name='download_json'),
    path('download/txt/', views.download_txt, name='download_txt'),
]
