from django import forms

from .models import Route
from .models import Weather


class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ('title',
                  'position1', 'position2', 'position3',
                  'position4', 'position5', 'position6',
                  'position7', 'position8', 'position9',
                  'position10',
                  'heading',)


class WeatherForm(forms.ModelForm):

    class Meta:
        model = Weather
        fields = ('title', 'temperature', 'wind', 'pressure', 'latitude', 'longitude',)
