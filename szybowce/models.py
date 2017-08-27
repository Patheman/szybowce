from django.db import models
from django.utils import timezone

# Create your models here.


#   information about the planned route

class Route(models.Model):
    lista= [];

    position1 = models.CharField(max_length=200)    
    #   the latitude and longitude you start from
    position2 = models.CharField(max_length=200)     
    position3 = models.CharField(max_length=200)     
    position4 = models.CharField(max_length=200)
    position5 = models.CharField(max_length=200)
    position6 = models.CharField(max_length=200)
    position7 = models.CharField(max_length=200)
    position8 = models.CharField(max_length=200)
    position9 = models.CharField(max_length=200)
    position10= models.CharField(max_length=200)
    
    heading1 = models.CharField(max_length=200)          #   the angle of the route   (NKDM)
    heading2 = models.CharField(max_length=200)
    heading3 = models.CharField(max_length=200)
    heading4 = models.CharField(max_length=200)
    heading5 = models.CharField(max_length=200)
    heading6 = models.CharField(max_length=200)
    heading7 = models.CharField(max_length=200)
    heading8 = models.CharField(max_length=200)
    heading9 = models.CharField(max_length=200)
    
    wind_speed = models.CharField(max_length=200)       #   (U)
    plane_speed = models.CharField(max_length=200)      #   (Vr)
    wind_angle = models.CharField(max_length=200)       #   (KW)
    
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
