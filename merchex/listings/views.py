from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return HttpResponse("<h1>Hello Django !</h1><p>Mes groupes préférés sont:</p>"
                        "<ul>"
                        f"  <li>{bands[0].name}</li>"
                        f"  <li>{bands[1].name}</li>"
                        f"  <li>{bands[2].name}</li>"
                        f"</ul>")


def about(request):
    return HttpResponse("<h1>Info</h1><p>We love merch</p>")


def listings(request):
    return HttpResponse("<h1>LISTINGS</h1><p>Voilà nos produits !</p>")


def contact(request):
    return HttpResponse("<h1>Contact us</h1><p>Formulaire de contact</p>")
