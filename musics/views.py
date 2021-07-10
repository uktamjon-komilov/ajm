from django.shortcuts import render, redirect


musics = [
    {
        "id": 1,
        "title": "Doston Ergashev - Uylanamiz",
        "file": "musiqalar/doston-ergashev-uylanamiz.mp3",
        "thumbnail": "rasmlar/1.jpg"
    },
    {
        "id": 2,
        "title": "Janob Rasul - Super",
        "file": "musiqalar/janob-rasul-super.mp3",
        "thumbnail": "rasmlar/2.jpg"
    },
    {
        "id": 3,
        "title": "Konfuz - Uti-putishka",
        "file": "musiqalar/konfuz-uti-putishka.mp3",
        "thumbnail": "rasmlar/3.jpg"
    }
]


def all_music(request):
    context = {
        "musics": musics
    }
    return render(request, "index.html", context)



def single_music(request, _id):
    music = list(filter(lambda music: music["id"] == _id, musics))
    if len(music) > 0:
        music = music[0]
    else:
        return redirect("home-page")
    
    context = {
        "music": music,
        "musics": musics
    }
    return render(request, "music.html", context)