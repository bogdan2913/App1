from turtle import title
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict = {
        'title': 'Домашняя страница',
        'content': 'Главная страница строительной аналитики',
        'list': [1, 2, 3],
        'dict': {1 : 'первый элемент', 2 : 'второй элемент'},
        'is_aunth': True
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')


