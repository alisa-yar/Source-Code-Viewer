from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect #added
from urllib.request import urlopen #added

def index(request):
    return render(request, "index.html")

def output(request):
    return render(request, "output.html")

def source(request): 
    url = request.POST.get('wanted_url')
    html = (urlopen(url)).read()
    return render(request, "output.html", {"html": html, "url": url})