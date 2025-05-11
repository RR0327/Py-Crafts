from django.urls import path
from . import views

urlpatterns = [
    path('', views.heatmap_view, name='heatmap'),
    path('weather/', views.weather_view, name='weather'),
]
