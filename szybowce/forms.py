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
                  'position10','wind_speed','plane_speed', 'wind_angle',
                  'heading1', 'heading2', 'heading3',
                  'heading4', 'heading5', 'heading6',
                  'heading7', 'heading8', 'heading9',)
   

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(RouteForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['title'].required = True
        self.fields['position1'].required = True
        self.fields['position2'].required = True
        self.fields['position3'].required = False
        self.fields['position4'].required = False
        self.fields['position5'].required = False
        self.fields['position6'].required = False
        self.fields['position7'].required = False
        self.fields['position8'].required = False
        self.fields['position9'].required = False
        self.fields['position10'].required = False
        self.fields['heading1'].required = True
        self.fields['heading2'].required = False
        self.fields['heading3'].required = False
        self.fields['heading4'].required = False
        self.fields['heading5'].required = False
        self.fields['heading6'].required = False
        self.fields['heading7'].required = False
        self.fields['heading8'].required = False
        self.fields['heading9'].required = False
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = 'Wymagane uzupełnienia.'




class WeatherForm(forms.ModelForm):

    class Meta:
        model = Weather
        fields = ('title', 'temperature', 'wind', 'pressure', 'latitude', 'longitude',)
