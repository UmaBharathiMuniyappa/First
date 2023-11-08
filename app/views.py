from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Jampandu(request):
    return HttpResponse('<h1><marquee>hi Jampandu how r u</h1></marquee>')