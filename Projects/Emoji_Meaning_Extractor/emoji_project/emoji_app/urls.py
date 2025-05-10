from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('history/', views.history_view, name='history'),
    path('top/', views.top_view, name='top'),
    path('about/', views.about_view, name='about'),
    path('download/', views.download_results, name='download_results'),
]
