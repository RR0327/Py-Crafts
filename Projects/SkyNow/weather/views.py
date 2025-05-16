import matplotlib
matplotlib.use('Agg')  # <- THIS LINE FIXES THE ERROR
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .scraper import get_weather_data
from .models import SearchHistory, TemperatureLog
from io import BytesIO
import base64
import json


def home(request):
    context = {}
    if request.method == "POST":
        country = request.POST.get("country")
        city = request.POST.get("city")
        data = get_weather_data(country, city)
        if data:
            SearchHistory.objects.create(city=city, country=country)
            TemperatureLog.objects.create(city=city, country=country, temperature=data["temperature"])
            context["weather"] = data
            context["city"] = city.title()
            context["country"] = country.title()
        else:
            context["error"] = "Weather data not found. Check the city/country name."

    context["recent_searches"] = SearchHistory.objects.all().order_by("-searched_at")[:5]
    return render(request, "weather/home.html", context)

def export_weather_json(request):
    latest = TemperatureLog.objects.last()
    if not latest:
        return JsonResponse({"error": "No data to export"}, status=404)

    data = {
        "city": latest.city,
        "country": latest.country,
        "temperature": latest.temperature,
        "recorded_at": latest.recorded_at.strftime("%Y-%m-%d %H:%M"),
    }
    return JsonResponse(data)

def export_weather_txt(request):
    latest = TemperatureLog.objects.last()
    if not latest:
        return HttpResponse("No data to export", content_type="text/plain")

    text = f"""Weather Report:
City: {latest.city.title()}
Country: {latest.country.title()}
Temperature: {latest.temperature}
Recorded at: {latest.recorded_at.strftime('%Y-%m-%d %H:%M')}
"""
    return HttpResponse(text, content_type="text/plain")

def trend_chart(request):
    logs = TemperatureLog.objects.order_by("-recorded_at")[:10][::-1]
    if not logs:
        return HttpResponse("No data to display.")

    timestamps = [log.recorded_at.strftime("%H:%M") for log in logs]
    temps = [int(''.join(filter(str.isdigit, log.temperature))) for log in logs]

    plt.figure(figsize=(8, 4))
    plt.plot(timestamps, temps, marker='o', color='blue')
    plt.title("Temperature Trend")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°F)")
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode()

    return render(request, "weather/trend.html", {"chart": img_str})
