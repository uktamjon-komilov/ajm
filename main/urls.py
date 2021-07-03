from django.contrib import admin
from django.urls import path
from .views import home, users_view, yakka_foydalanuvchi, yakka_foydalanuvchi_string

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("users/", users_view),
    path("users/<int:son>/", yakka_foydalanuvchi),
    path("users/<ism>/", yakka_foydalanuvchi_string),
]