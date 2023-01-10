from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def a1_first(request):
    return HttpResponse('<h1> This is first view</h1>')

def a1_second(request):
    return HttpResponse('<h1> This is second view</h1>')