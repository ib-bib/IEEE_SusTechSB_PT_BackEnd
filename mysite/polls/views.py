from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return HttpResponse('Hello Django, this is the index page of the polls app')

# Create your views here.
