from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>this is index.py</h1>')
def about(requset):
    return HttpResponse('<h1>this is about.py</h1>')
                        
def contact(request):
    return HttpResponse('<h1>this is contact page</h1>')