from django.shortcuts import render


def all_music(request):
    context = {
        "count": 5,
        "qoshiqlar": [
            {
                "id": 1,
                "title": "Till I collapse",
                "artist": "Eminem",
                "album": "Rock musics"
            },
            {
                "id": 2,
                "title": "Guli",
                "artist": "Jahongir Poziljonov",
                "album": "To'ybop"
            },
            {
                "id": 4,
                "title": "I am not Afraid",
                "artist": "Eminem",
                "album": "Rock musics"
            },
            {
                "id": 9,
                "title": "Lose yourself",
                "artist": "Eminem",
                "album": "Rock musics"
            },
        ]
    }
    return render(request, "index.html", context)