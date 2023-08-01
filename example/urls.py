# example/urls.py
from django.urls import path
from example.views import index, output
from . import views

urlpatterns = [
    path('', index, name="index"),
    path("output/", views.source, name="output"),
]
