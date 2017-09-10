from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.route_list, name='route_list'),
    url(r'^route/(?P<pk>[0-9]+)/$', views.route_detail, name='route_detail'),
    url(r'^route/new/$', views.route_new, name='route_new'),
    url(r'^route/(?P<pk>[0-9]+)/edit/$', views.route_edit, name='route_edit'),
    url(r'^route/(?P<pk>[0-9]+)/pdf/$', views.pdf_gen, name='pdf_gen'),
]
