from django.urls import path
from .views import *

urlpatterns = [
    path("", all_movies),
    path("1/", single_movies),
    path("netflix/", netflix_movies)
]