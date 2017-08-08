from django import template
import math
register = template.Library()

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



###########################  PRĘDKOŚĆ PODRÓŻNA  ###########################
@register.filter(name='ground_speed')
def ground_speed(W2, Vr):
    return float(Vr) + float(W2)

@register.filter(name='ground_speed2')
def ground_speed2(U, KW):
    return float(U)*math.cos(float(KW))
###########################################################################



###########################  KĄT ZNOSZENIA  ###############################
@register.filter(name='angle_z')
def angle_z(K2, U):
    return math.asin(float(U)*float(K2))

@register.filter(name='angle_z2')
def angle_z2(KW, Vr):
    return math.sin(float(KW))/float(Vr)
###########################################################################



###########################  KĄT MAGNETYCZNY  #############################
@register.filter(name='angle_m')
def angle_m(NKDM, KZ):
    return float(NKDM) + float(KZ)
###########################################################################



###########################  CZAS  ########################################
@register.filter(name='time')
def time(V, S):
    return float(S)/float(V)
###########################################################################


