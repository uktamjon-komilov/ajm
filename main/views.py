from django.http.response import HttpResponse

def home(request):
    word = request.GET.get("q", None)
    if word:
        return HttpResponse(word)
    else:
        return HttpResponse("Free")


def users_view(request):
    return HttpResponse("Foydalanuvchilar")


def yakka_foydalanuvchi(request, son):
    return HttpResponse(f"Qaysidir foydalanuvchi - {son}")


def yakka_foydalanuvchi_string(request, ism):
    return HttpResponse(f"Ism: {ism}")