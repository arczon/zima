from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(reguest):
    return render(reguest, 'zegar/index.html', {})