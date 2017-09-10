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
    if p1 and p2:
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
            return round(vincenty(first, second).kilometers, 2)
        else:
            return ''
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
        data = location.raw
        data = data['address']
        where = ''
        if 'city' in data.keys():
            where = where + " | " + data['city']
        elif 'town' in data.keys():
            where = where + " | " + data['town']
        elif 'village' in data.keys():
            where = where + " | " + data['village']
        if 'county' in data.keys():
            where = where + " | " + data['county']
        if 'state' in data.keys():
            where = where + " | " + data['state']
        if 'country' in data.keys():
            where = where + " | " + data['country']
        return where + " | "
        #return location.address
    else:
        return ''
###################################################################################



###########################  PRĘDKOŚĆ PODRÓŻNA  ###########################
@register.filter(name='ground_speed')
def ground_speed(W2, Vr):
    if W2 and Vr:
        return round(float(Vr) + float(W2), 2)
    else:
        return ''
@register.filter(name='ground_speed2')
def ground_speed2(KW, U):
    if KW and U:
        return float(U)*math.cos(math.radians(float(KW)))
    else:
        return ''
###########################################################################



###########################  UZUPEŁNIJ KĄT  ###############################
@register.filter(name='angle_add')
def angle_add(KW, NKDW):
    if KW and NKDW:
        a = float(KW) - float(NKDW)
        if abs(float(a)) < 180.0:
            return a
        else:
            if float(a) > 0:
                return math.copysign(360.0 - abs(float(a)), -1)
            else:
                return 360.0 - abs(float(a))
    else:
        return ''

###########################################################################



###########################  KĄT ZNOSZENIA  ###############################
@register.filter(name='angle_z')
def angle_z(K2, U):
    if K2 and U:
        return round(math.degrees(math.asin(float(U)*float(K2))), 2)
    else:
        return ''

@register.filter(name='angle_z2')
def angle_z2(KW, Vr):
    if KW and Vr:
        return  math.sin(math.radians(float(KW)))/float(Vr)
    else:
        return ''
###########################################################################



###########################  KĄT MAGNETYCZNY  #############################
@register.filter(name='angle_m')
def angle_m(KZ, NKDM):
    if NKDM:
        return round(float(KZ) + float(NKDM), 2)
    else:
        return ''
###########################################################################



###########################  CZAS  ########################################
@register.filter(name='time')
def time(V, S):
    if V and S:
        return round(float(S)/float(V), 2)
    else:
        return ''
@register.filter(name='time1')
def time1(V, S1):
    if V and S1:
        return str(V) + '|' + str(S1)
    else:
        return ''
@register.filter(name='time2')
def time2(t1, S2):
    if t1 and S2:
        my_string = t1.split('|')
        V = float(my_string[0])
        S1 = my_string[1]
        
        p1_string = S1.split( )
        p1_lat = p1_string[0]
        p1_lon = p1_string[1]
        f_p1_lon = float(p1_lon)
        f_p1_lat = float(p1_lat)

        p2_string = S2.split( )
        p2_lat = p2_string[0]
        p2_lon = p2_string[1]
        f_p2_lon = float(p2_lon)
        f_p2_lat = float(p2_lat)


        if f_p1_lat and f_p1_lon and f_p2_lat and f_p2_lon:
            first = (f_p1_lat, f_p1_lon)
            second = (f_p2_lat, f_p2_lon)
            S = round(vincenty(first, second).kilometers, 2)
         
        return round(float(S)/float(V), 2)
    else:
        return ''
###########################################################################


###########################  OBLICZANIE ODLEGŁOŚCI  ######################
@register.filter(name='calc_dist')
def calc_dist(p1, p2):
    if p1 and p2:
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
            return round(vincenty(first, second).kilometers, 2)
        else:
            return ''
    else:
        return ''
##########################################################################
