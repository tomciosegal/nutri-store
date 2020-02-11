from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')