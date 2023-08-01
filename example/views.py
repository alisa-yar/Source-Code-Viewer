from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect #added
import requests #added
from bs4 import BeautifulSoup #added
# from urllib.request import urlopen #added
# from gazpacho import get, Soup #added

def index(request):
    return render(request, "index.html")

def output(request):
    return render(request, "output.html")

def source(request): 
    url = request.POST.get('wanted_url')
    # html = (urlopen(url)).read()
    r = requests.get(url) # Get URL Content
    soup = BeautifulSoup(r.content, 'html.parser') # Parse HTML Code
    html = soup.prettify()
    print(html)
    return render(request, "output.html", {"url": url, "html": html})