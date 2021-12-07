from django.http import HttpResponse
# qqqqqqqqqqdfgsd

def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница')
