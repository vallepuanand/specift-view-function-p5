from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def a2_first(request):
    return HttpResponse('<h1>this is for app2 first view ')

def a2_second(request):
    return HttpResponse('<h1>this is for app2 second view ')