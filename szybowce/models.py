from django.db import models
from django.utils import timezone

# Create your models here.


#   information about the planned route

class Route(models.Model):
    
    start_lat = models.FloatField()     #   the latitude you start from
    start_long = models.FloatField()    #   the longitude
    
    end_lat = models.FloatField()
    end_long = models.FloatField()
    
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title


#   wheater conditions change

class Weather(models.Model):
    
    wind = models.FloatField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
