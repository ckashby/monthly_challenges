from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        # return HttpResponse(monthly_challenges[months[month - 1]])
        redirect_month = months[month - 1]
        return HttpResponseRedirect("/challenges/" + redirect_month)  # Update using f-string TODO:

    except:
        return HttpResponseNotFound("This month is not supported!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
