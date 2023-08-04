from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect #added
import requests #added
from bs4 import BeautifulSoup #added

def index(request):
    return render(request, "index.html")

def output(request):
    return render(request, "output.html")

def search(request):
    return render(request, "search.html")

def source(request): 
    url = request.POST.get('wanted_url')
    r = requests.get(url) # Get URL Content
    soup = BeautifulSoup(r.content, 'html.parser') # Parse HTML Code
    html = soup.prettify()
    print(html)
    return render(request, "output.html", {"url": url, "html": html})

def find_query(request):
    query = request.POST.get('wanted_search')
    html = request.POST.get('current_html')
    findAll = html.find_all(query)
    return render(request, "output.html", {"query": query, "findAll": findAll})

# def source(url): 
#     html = requests.get(url) # Get URL Content
#     soup = BeautifulSoup(html.content, 'html.parser') # Parse HTML Code
#     # html = soup.prettify()
#     print(soup)

# def search(url, query):
#     html = requests.get(url)
#     soup = BeautifulSoup(html.content, 'html.parser')
#     elements_list = soup.find_all(query)
#     for element in elements_list:
#         print(element)