from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('Page with courses')
# Create your views here.
