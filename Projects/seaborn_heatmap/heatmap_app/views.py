# seaborn_heatmap/views.py
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import HeatmapForm, WeatherForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

heatmap_history = []

def generate_heatmap(data, cmap, annot, filename):
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, cmap=cmap, annot=annot, fmt=".2f")
    plt.title("Generated Heatmap")
    save_path = os.path.join(STATIC_DIR, filename)
    plt.savefig(save_path)
    plt.close()
    return filename

def heatmap_view(request):
    image_filename = None
    csv_data = None
    history = heatmap_history[-5:]  # show last 5 heatmaps
    if request.method == 'POST':
        form = HeatmapForm(request.POST, request.FILES)
        if form.is_valid():
            rows = form.cleaned_data['rows']
            cols = form.cleaned_data['cols']
            cmap = form.cleaned_data['colormap']
            annot = form.cleaned_data['annot']
            seed = form.cleaned_data['random_seed']
            csv_file = form.cleaned_data['csv_file']

            if seed is not None:
                np.random.seed(seed)

            if csv_file:
                fs = FileSystemStorage()
                filename = fs.save(csv_file.name, csv_file)
                file_path = fs.path(filename)
                csv_data = pd.read_csv(file_path)
                data = csv_data.values
            else:
                data = np.random.rand(rows, cols)

            image_filename = generate_heatmap(data, cmap, annot, "heatmap.png")
            heatmap_history.append(image_filename)
    else:
        form = HeatmapForm()

    return render(request, 'heatmap_app/heatmap.html', {
        'form': form,
        'image_filename': image_filename,
        'csv_data': csv_data,
        'history': history
    })

def weather_view(request):
    weather = None

    # Mapping human-friendly names to URL-friendly slugs
    COUNTRY_CODES = {
        'england': 'uk',
        'united kingdom': 'uk',
        'uk': 'uk',
        'united states': 'usa',
        'usa': 'usa',
        'germany': 'germany',
        'bangladesh': 'bangladesh',
        'canada': 'canada',
        'australia': 'australia',
        'india': 'india',
        # Add more as needed
    }

    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            country_input = form.cleaned_data['country'].lower().strip()
            city = form.cleaned_data['city'].lower().replace(" ", "-")
            country = COUNTRY_CODES.get(country_input, country_input)

            url = f"https://www.timeanddate.com/weather/{country}/{city}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                temperature = soup.find('div', class_='h2').get_text(strip=True)
                weather_description = soup.find('div', class_='h2').find_next('p').get_text(strip=True)
                weather = {
                    'city': city.replace('-', ' ').title(),
                    'country': country_input.title(),
                    'temperature': temperature,
                    'description': weather_description
                }
            except AttributeError:
                weather = {'error': "City or country not found. Try using official country name or code (e.g., 'uk', 'usa')."}
    else:
        form = WeatherForm()

    return render(request, 'heatmap_app/weather.html', {'form': form, 'weather': weather})
