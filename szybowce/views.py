import os
import reportlab
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Route
from .models import Weather
from .forms import WeatherForm
from .forms import RouteForm
from .templatetags import first 
from django.shortcuts import redirect
#from .find_location import run
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
pdfmetrics.registerFont(TTFont('Pacifico', 'Pacifico-Regular.ttf'))

# Create your views here.


def route_list(request):

    routes = Route.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'szybowce/route_list.html', {'routes': routes})

def pdf_gen(request, pk):
    # Create the HttpResponse object with the appropriate PDF headers.
     response = HttpResponse(content_type='application/pdf')
     response['Content-Disposition'] = 'attachment; filename="twoja_trasa.pdf"'
     # Create the PDF object, using the response object as its "file."
     p = canvas.Canvas(response)
     p.setFont("Pacifico", 32)
     p.drawString(400, 800, "ppszybowce")

     p.setFont("Verdana", 12)
     # Get the Route object
     route = get_object_or_404(Route, pk=pk)

     # Draw things on the PDF. Here's where the PDF generation happens.
     # See the ReportLab documentation for the full list of functionality.
     x=2 
     p.drawString(25, 800-25*x, "TWOJA TRASA:")
     x=3
     if route.position1:
        p.drawString(25, 800-25*x, "Pozycja 1:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position1))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading1)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading1), route.wind_speed), route.plane_speed), route.position1), route.position2)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position1, route.position2)))
        x=x+3
     if route.position2:
        p.drawString(25, 800-25*x, "Pozycja 2:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position2))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading2)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading2), route.wind_speed), route.plane_speed), route.position2), route.position3)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position2, route.position3)))
        x=x+3
     if route.position3:
        p.drawString(25, 800-25*x, "Pozycja 3:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position3))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading3)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading3), route.wind_speed), route.plane_speed), route.position3), route.position4)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position3, route.position4)))
        x=x+3
     if route.position4:
        p.drawString(25, 800-25*x, "Pozycja 4:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position4))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading4)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading4), route.wind_speed), route.plane_speed), route.position4), route.position5)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position4, route.position5)))
        x=x+3
     if route.position5:
        p.drawString(25, 800-25*x, "Pozycja 5:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position5))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading5)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading5), route.wind_speed), route.plane_speed), route.position5), route.position6)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position5, route.position6)))
        x=x+3
     if route.position6:
        p.drawString(25, 800-25*x, "Pozycja 6:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position6))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading6)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading6), route.wind_speed), route.plane_speed), route.position6), route.position7)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position6, route.position7)))
        x=x+3
     if route.position7:
        p.drawString(25, 800-25*x, "Pozycja 7:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position7))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading7)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading7), route.wind_speed), route.plane_speed), route.position7), route.position8)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position7, route.position8)))
        x=x+3
     if route.position8:
        p.drawString(25, 800-25*x, "Pozycja 8:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position8))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading8)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading8), route.wind_speed), route.plane_speed), route.position8), route.position9)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position8, route.position9)))
        x=x+3
     if route.position9:
        p.drawString(25, 800-25*x, "Pozycja 9:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position9))
        p.drawString(25, 800-25*(x+1), "Kąt [*]:")
        p.drawString(90, 800-25*(x+1), str(first.angle_m(first.angle_z(first.angle_z2(route.wind_angle, route.plane_speed), route.wind_speed), route.heading9)))
        p.drawString(150, 800-25*(x+1), "Czas [h]:")
        p.drawString(225, 800-25*(x+1), str(first.time2(first.time1(first.ground_speed(first.ground_speed2(first.angle_add(route.wind_angle, route.heading9), route.wind_speed), route.plane_speed), route.position9), route.position10)))
        p.drawString(275, 800-25*(x+1), "Odległość [km]:")
        p.drawString(390, 800-25*(x+1), str(first.calc_dist(route.position9, route.position10)))
        x=x+3
     if route.position10:
        p.drawString(25, 800-25*x, "Pozycja 10:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position10))

     
     # Close the PDF object cleanly, and we're done.
     p.showPage()
     p.save()
     return response

def route_detail(request, pk):
    
    route = get_object_or_404(Route, pk=pk)
    return render(request, 'szybowce/route_detail.html', {'route': route})
    

@login_required
def route_new(request):

    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit=False)
            route.author = request.user
            route.published_date = timezone.now()
            route.save()
            return redirect('route_detail', pk=route.pk)
    else:
        form = RouteForm()
    return render(request, 'szybowce/route_edit.html', {'form': form})


@login_required
def route_edit(request, pk):

    route = get_object_or_404(Route, pk=pk)
    if request.method == "POST":
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            route = form.save(commit=False)
            route.author = request.user
            route.published_date = timezone.now()
            route.save()
            return redirect('route_detail', pk=route.pk)
    else:
        form = RouteForm(instance=route)
    return render(request, 'szybowce/route_edit.html', {'form': form})


@login_required
def route_remove(request, pk):
    route = get_object_or_404(Route, pk=pk)
    route.delete()
    return redirect('route_list')
