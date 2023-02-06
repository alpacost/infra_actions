from django.http import HttpResponse


def index(request):
    return HttpResponse('Оффициально заявляю, шо хотово!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
