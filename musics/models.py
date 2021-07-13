from django.db import models


class Artist(models.Model):
    fullname = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    rating = models.FloatField(default=3)
    data_of_birth = models.DateField(blank=True, null=True)

    GENDER = [
        ("m", "male"),
        ("f", "female")
    ]
    gender = models.CharField(choices=GENDER, max_length=255, blank=True, default="m")


class Music(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)