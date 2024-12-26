from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create a view for index page
def index(request):
    return HttpResponse("Hola perros!")

def jan(request):
    return HttpResponse("This is the January page")
