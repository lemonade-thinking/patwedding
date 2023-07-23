from django.shortcuts import render
from django.views.generic import TemplateView
# from django.http import HttpResponse

# Create your views here

# def homePageView(request):
#     return HttpResponse("Hello, world!")

class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class EventPageView(TemplateView):
    template_name = "wedding_day.html"

class LocationsPageView(TemplateView):
    template_name = "locations.html"