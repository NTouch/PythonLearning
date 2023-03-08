from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello Django !</h1>")


def about(request):
    return HttpResponse("<h1>Info</h1><p>We love merch</p>")


def listings(request):
    return HttpResponse("<h1>LISTINGS</h1><p>Voilà nos produits !</p>")


def contact(request):
    return HttpResponse("<h1>Contact us</h1><p>Formulaire de contact</p>")
