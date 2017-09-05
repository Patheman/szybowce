from django import template
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import math

register = template.Library()
geolocator = Nominatim()


@register.filter(name='nowy')
def nowy(value):
    return "dziala: %s" % value

@register.filter(name='divide_lat')
def divide_lat(value, arg):
    original_string = value
    max_length = arg
    if len(original_string) <= max_length:
        original_float = float(original_string)
        return original_float
    else:
        original_float = float(original_string[:max_length])
        return original_float

@register.filter(name='divide_lon')
def divide_lon(value, arg):
    original_string = value
    max_length = arg
    if len(original_string) <= max_length:
        original_float = float(original_string)
        return original_float
    else:
        original_float = float(original_string[-max_length:])
        return original_float


#   Tworzenie roznych funkcji, które będą zwracały wynik działania matematycznego, np. dodawanie:

@register.filter(name='adding')
def adding(value, arg):
    original_string = value
    max_length = 3
    # jesli wartosc sklada sie tylko z jednej liczby to zwroc ja
    if len(original_string) <= max_length:
        original_float = float(original_string)
        return original_float
    # w przeciwnym wypadku wyciagnij latitude i longitude
    else:
        first_list = value.split( )
        second_list = arg.split( )
        first_lat = float(first_list[0])
        first_lon = float(first_list[1])
        second_lat = float(second_list[0])
        second_lon = float(second_list[1])
        return first_lat + second_lat




###########################  OBLICZANIE ODLEGŁOŚCI  ######################
@register.filter(name='calc_dist')
def calc_dist(p1, p2):
    p1_string = p1.split( )
    p1_lat = p1_string[0]
    p1_lon = p1_string[1]
    f_p1_lat = float(p1_lat)
    f_p1_lon = float(p1_lon)

    p2_string = p2.split( )
    p2_lat = p2_string[0]
    p2_lon = p2_string[1]
    f_p2_lat = float(p2_lat)
    f_p2_lon = float(p2_lon)
    
    if f_p1_lat and f_p1_lon and f_p2_lat and f_p2_lon:
        first = (f_p1_lat, f_p1_lon)
        second = (f_p2_lat, f_p2_lon)
        return vincenty(first, second).kilometers
    else:
        return ''
##########################################################################



###########################  DODANIE NAZW MIEJSCOWOŚCI  ###########################
@register.filter(name='gps_name')
def gps_name(arg):
    if arg:
        original_string = arg
        my_list = arg.split( )
        lat = my_list[0]
        lon = my_list[1]
        location = geolocator.reverse("%s, %s" % (lat, lon))
        return location.address
    else:
        return ''
###################################################################################



###########################  PRĘDKOŚĆ PODRÓŻNA  ###########################
@register.filter(name='ground_speed')
def ground_speed(W2, Vr):
    return round(float(Vr) + float(W2), 2)

@register.filter(name='ground_speed2')
def ground_speed2(U, KW):
    return float(U)*math.cos(math.radians(float(KW)))
###########################################################################



###########################  KĄT ZNOSZENIA  ###############################
@register.filter(name='angle_z')
def angle_z(K2, U):
    return round(math.degrees(math.asin(float(U)*float(K2))), 2)

@register.filter(name='angle_z2')
def angle_z2(KW, Vr):
    return  math.sin(math.radians(float(KW)))/float(Vr)
###########################################################################



###########################  KĄT MAGNETYCZNY  #############################
@register.filter(name='angle_m')
def angle_m(KZ, NKDM):
    if NKDM:
        return round(float(NKDM) + float(KZ), 2)
    else:
        return ''
###########################################################################



###########################  CZAS  ########################################
@register.filter(name='time')
def time(S, V):
    if V and S:
        return round(float(S)/float(V), 2)
    else:
        return ''
###########################################################################


