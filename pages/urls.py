from django.urls import path
from .views import HomePageView, AboutPageView, home

urlpatterns = [
    path("", home, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
