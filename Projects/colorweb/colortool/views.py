from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils import (
    color_name_to_code, is_valid_color_name, name_to_rgb_code,
    hex_to_rgb_code, rgb_to_hex_code, closest_color_name,
    generate_theme_from_base_color
)
import json

def index(request):
    results = None

    if request.method == "POST":
        color_name = request.POST.get("color_name")
        hex_code = request.POST.get("hex_code")
        rgb_input = request.POST.get("rgb_code")

        try:
            rgb_tuple = tuple(map(int, rgb_input.split(','))) if rgb_input else None
        except:
            rgb_tuple = None

        results = {}

        if color_name:
            results['HEX from Name'] = color_name_to_code(color_name)
            results['RGB from Name'] = name_to_rgb_code(color_name)
            results['Theme'] = generate_theme_from_base_color(color_name)

        if hex_code:
            results['RGB from HEX'] = hex_to_rgb_code(hex_code)

        if rgb_tuple:
            results['HEX from RGB'] = rgb_to_hex_code(rgb_tuple)
            results['Closest Color Name'] = closest_color_name(rgb_tuple)

        request.session['results'] = results

    return render(request, 'colortool/index.html', {'results': results})

def download_json(request):
    data = request.session.get('results', {})
    return JsonResponse(data, json_dumps_params={'indent': 4})

def download_txt(request):
    data = request.session.get('results', {})
    txt = '\n'.join(f"{k}: {v}" for k, v in data.items())
    return HttpResponse(txt, content_type='text/plain')
