from django import template

register = template.Library()

@register.filter("joriy_yol")
def joriy_yol(request):
    path = str(request.path)
    path = path[1:-1]
    return int(path)