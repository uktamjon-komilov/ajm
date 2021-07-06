from django.urls import path
from .views import *

urlpatterns = [
    path("", all_music),
    # path("1/", single_music),
]