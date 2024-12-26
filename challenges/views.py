from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# def index(request):
#     return HttpResponse("Hola amigos!")

def monthly_challenge(request, month):
    if month == 'jan':
        challenge_text = "This is the January challenge"
    elif month == 'feb':
        challenge_text = "This is the February test"
    elif month == 'mar':
        challenge_text = "This is the March goal"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)

