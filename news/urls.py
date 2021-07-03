from django.urls import path
from .views import *

urlpatterns = [
    path("", all_news),
    path("1/", single_news),
]