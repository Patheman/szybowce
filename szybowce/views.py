from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Route
from .models import Weather
from .forms import WeatherForm
from .forms import RouteForm
from django.shortcuts import redirect
#from .find_location import run


# Create your views here.


def route_list(request):

    routes = Route.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'szybowce/route_list.html', {'routes': routes})


def route_detail(request, pk):

    route = get_object_or_404(Route, pk=pk)
    
    return render(request, 'szybowce/route_detail.html', {'route': route})
    


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
