from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hola estudiantes!')

def jan(request):
    return HttpResponse('Este es el reto de enero')
