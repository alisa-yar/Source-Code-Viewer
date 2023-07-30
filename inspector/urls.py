from django.urls import path
from . import views

urlpatterns = [
    # input page - display the page with the form for the URL input
    # output page - display the html code that we got from the URL
    path("", views.index, name="index"),
    path("output/", views.source, name="output"),
]