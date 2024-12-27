from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import Http404 

monthly_challenges = {
    "jan": "Eat no meat for the entire month",
    "feb": "Walk for at least 20 minutes every day",
    "mar": "Study Django for at least 20 minutes every day",
    "apr": "Eat no meat for the entire month",
    "may": "Swim for at least 20 minutes every day",
    "jun": "Study Django for at least 20 minutes every day",
    "jul": "Eat no meat for the entire month",
    "aug": "Read a book for at least 1 hour every day",
    "sep": "Study Django for at least 20 minutes every day",
    "oct": "Eat no meat for the entire month",
    "nov": "Surf for at least 20 minutes every day",
    # "dec": "This is the December goal"
    "dec": None
}


def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Invalid month.")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404() # This will raise a 404 error page from /templates/404.html
