from django.shortcuts import render


def all_music(request):
    context = {
        "xabarlar": [
            {"text": "Salom mening ismim Uktamjon", "type": "yaxshi", "time": "12:45"},
            {"text": "Men dasturchi bo'lmoqchiman", "type": "yomon"},
            {"text": "men ypozdim", "type": "yaxshi"},
            {"text": "Jahongir aka obi hao qle", "type": "yomon"}
        ]
    }
    return render(request, "index.html", context)