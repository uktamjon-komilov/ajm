from django.shortcuts import render
from django.http import HttpResponse

def all_movies(request):
    return HttpResponse("Barcha kinolar")

def single_movies(request):
    return HttpResponse("Bitta kino")



def netflix_movies(request):
    return HttpResponse("Netflix Originals")