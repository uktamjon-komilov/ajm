from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movies/", include("movies.urls")),
    path("musics/", include("musics.urls")),
    path("news/", include("news.urls")),
]