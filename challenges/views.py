from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# create a python array with the months of the year as keys and examples of challenges as values
monthly_challenges = {
    "jan": "This is the January challenge",
    "feb": "This is the February test",
    "mar": "This is the March goal",
    "apr": "This is the April challenge",
    "may": "This is the May test",
    "jun": "This is the June goal",
    "jul": "This is the July challenge",
    "aug": "This is the August test",
    "sep": "This is the September goal",
    "oct": "This is the October challenge",
    "nov": "This is the November test",
    "dec": "This is the December goal"
}

# def index(request):
#     return HttpResponse("Hola amigos!")


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
