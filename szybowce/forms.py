from django import forms

from .models import Route
from .models import Weather


class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ('title', 'start_lat', 'start_long', 'end_lat', 'end_long',)


class WeatherForm(forms.ModelForm):

    class Meta:
        model = Weather
        fields = ('title', 'temperature', 'wind', 'pressure', 'latitude', 'longitude',)
