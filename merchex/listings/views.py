from django.shortcuts import render
from listings.models import Band, Listing


# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    return render(request, "listings/about.html")


def listings(request):
    listing = Listing.objects.all()
    return render(request, "listings/listings.html", {"listing": listing})


def contact(request):
    return render(request, "listings/contact.html")
