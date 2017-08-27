from django.contrib import admin
from .models import Route
from .models import Weather

# Register your models here.
admin.site.register(Route)
admin.site.register(Weather)
