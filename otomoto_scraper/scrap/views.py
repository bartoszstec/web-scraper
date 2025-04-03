from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    return render(request, 'index.html')

def scraping(request):
    # Making a GET request
    r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
    print(r)
    print(r.content)
    if r.status_code == 200:
        return HttpResponse(r.text)
    else:
        return render(request, 'error.html', {'status_code': r.status_code})

def error(request):
    return render(request, 'error.html')