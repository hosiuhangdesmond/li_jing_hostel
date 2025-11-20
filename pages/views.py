from django.shortcuts import render
from listings.models import Listing
from managers.models import Manager
from listings.choices import district_choices, room_choices, rooms_choices
#from django.http import HttpResponse
# Create your views here.

def index(request):
    listings = Listing.objects.filter(is_published=True)[:3]
    context = {"listings":listings,
            "district_choices":district_choices,
            "room_choices":room_choices,
            "rooms_choices":rooms_choices
            }
    return render(request, 'pages/index.html', context)

def about(request):
    managers = Manager.objects.order_by("-hire_date")[:3]
    mvp_managers = Manager.objects.all().filter(is_mvp=True)
    context = {
        "managers": managers,
        "mvp_managers": mvp_managers
    }
    return render(request, 'pages/about.html', context)


def office_style(request):
    return render(request, 'pages/office_style.html')

def romantic_style(request):
    return render(request, 'pages/romantic_style.html')

def family_friendly(request):
    return render(request, 'pages/family_friendly.html')

def study_focused(request):
    return render(request, 'pages/study_focused.html')

def room_prices(request):
    return render(request, 'pages/room_prices.html')

def personal_data(request):
    return render(request, 'pages/personal_data.html')

def disclaimer(request):
    return render(request, 'pages/disclaimer.html')
