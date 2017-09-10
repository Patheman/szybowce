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
     p.setFont("Verdana", 12)
     # Get the Route object
     route = get_object_or_404(Route, pk=pk)

     # Draw things on the PDF. Here's where the PDF generation happens.
     # See the ReportLab documentation for the full list of functionality.
     
     p.drawString(25, 800, "TWOJA TRASA:")
     x=2
     if route.position1:
        p.drawString(25, 800-25*x, "Pozycja 1:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position1))
        p.drawString(25, 800-25*(x+1), "Kąt 1:")
        p.drawString(100, 800-25*(x+1), route.heading1)
        x=x+2
     if route.position2:
        p.drawString(25, 800-25*x, "Pozycja 2:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position2))
        p.drawString(25, 800-25*(x+1), "Kąt 2:")
        p.drawString(100, 800-25*(x+1), route.heading2)
        x=x+2
     if route.position3:
        p.drawString(25, 800-25*x, "Pozycja 3:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position3))
        p.drawString(25, 800-25*(x+1), "Kąt 3:")
        p.drawString(100, 800-25*(x+1), route.heading3)
        x=x+2
     if route.position4:
        p.drawString(25, 800-25*x, "Pozycja 4:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position4))
        p.drawString(25, 800-25*(x+1), "Kąt 4:")
        p.drawString(100, 800-25*(x+1), route.heading4)
        x=x+2
     if route.position5:
        p.drawString(25, 800-25*x, "Pozycja 5:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position5))
        p.drawString(25, 800-25*(x+1), "Kąt 5:")
        p.drawString(100, 800-25*(x+1), route.heading5)
        x=x+2
     if route.position6:
        p.drawString(25, 800-25*x, "Pozycja 6:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position6))
        p.drawString(25, 800-25*(x+1), "Kąt 6:")
        p.drawString(100, 800-25*(x+1), route.heading6)
        x=x+2
     if route.position7:
        p.drawString(25, 800-25*x, "Pozycja 7:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position7))
        p.drawString(25, 800-25*(x+1), "Kąt 7:")
        p.drawString(100, 800-25*(x+1), route.heading7)
        x=x+2
     if route.position8:
        p.drawString(25, 800-25*x, "Pozycja 8:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position8))
        p.drawString(25, 800-25*(x+1), "Kąt 8:")
        p.drawString(100, 800-25*(x+1), route.heading8)
        x=x+2
     if route.position9:
        p.drawString(25, 800-25*x, "Pozycja 9:") 
        p.drawString(100, 800-25*x, first.gps_name(route.position9))
        p.drawString(25, 800-25*(x+1), "Kąt 9:")
        p.drawString(100, 800-25*(x+1), route.heading4)
        x=x+2
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
