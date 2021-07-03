from django.shortcuts import render
from django.http import HttpResponse

def all_news(request):
    return HttpResponse("Barcha yangiliklar")

def single_news(request):
    return HttpResponse("Bitta yangilik")