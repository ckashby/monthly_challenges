from django.shortcuts import render
from django.http import HttpResponse

# Create a view for index page


def index(request):
    return HttpResponse("Hola amigos!")

def jan(request):
    return HttpResponse("This is the January page")
