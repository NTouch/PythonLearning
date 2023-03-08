from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    return HttpResponse("<h1>Info</h1><p>We love merch</p>")


def listings(request):
    listing = Listing.objects.all()
    return HttpResponse("<h1>LISTINGS</h1><p>Voilà nos produits :</p>"
                        "<ul>"
                        f"  <li>{listing[0].title}</li>"
                        f"  <li>{listing[1].title}</li>"
                        f"  <li>{listing[2].title}</li>"
                        f"  <li>{listing[3].title}</li>"
                        "</ul>")


def contact(request):
    return HttpResponse("<h1>Contact us</h1><p>Formulaire de contact</p>")
