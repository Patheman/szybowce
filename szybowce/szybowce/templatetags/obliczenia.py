from django import template
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

