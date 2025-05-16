from django.urls import path
from .views import home, export_weather_json, export_weather_txt, trend_chart

urlpatterns = [
    path('', home, name='home'),
    path('export/json/', export_weather_json, name='export_json'),
    path('export/txt/', export_weather_txt, name='export_txt'),
    path('trend/', trend_chart, name='trend'),
]
