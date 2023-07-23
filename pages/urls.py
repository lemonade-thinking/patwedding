from django.urls import path
from .views import HomePageView, AboutPageView
from .views import EventPageView, LocationsPageView

urlpatterns = [
    path("locations/", LocationsPageView.as_view(), name="locations"),
    path("wedding_day/", EventPageView.as_view(), name="wedding_day"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home")
]