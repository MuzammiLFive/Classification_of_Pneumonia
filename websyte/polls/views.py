from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<marquee direction=\"scroll\"><h1>HOLY SHIT ITS WORKING</h1></marquee>")