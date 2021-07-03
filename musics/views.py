from django.shortcuts import render
from django.http import HttpResponse

def all_music(request):
    return HttpResponse("Barcha musiqalar")

def single_music(request):
    return HttpResponse("Bitta musiqa")