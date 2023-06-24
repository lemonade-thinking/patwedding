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