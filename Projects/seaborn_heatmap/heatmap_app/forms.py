from django import forms

COLORMAPS = [
    ('coolwarm', 'Coolwarm'),
    ('viridis', 'Viridis'),
    ('plasma', 'Plasma'),
    ('magma', 'Magma'),
    ('cividis', 'Cividis'),
]

class HeatmapForm(forms.Form):
    rows = forms.IntegerField(min_value=1, max_value=100, initial=10, label='Rows')
    cols = forms.IntegerField(min_value=1, max_value=100, initial=10, label='Columns')
    colormap = forms.ChoiceField(choices=COLORMAPS, initial='coolwarm')
    annot = forms.BooleanField(required=False, label='Show Annotations')
    random_seed = forms.IntegerField(required=False, label='Random Seed')
    csv_file = forms.FileField(required=False, label='Upload CSV')

class WeatherForm(forms.Form):
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
