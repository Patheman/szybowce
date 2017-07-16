from django import forms

from .models import Route

class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ('title', 'start_lat', 'start_long', 'end_lat', 'end_long',)
