from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, David!!!")


def index2(request):
    return HttpResponse("<h1>Hello, David!!!</h1>")


def index3(request):
    msg = 'This is my message!!!'
    return render(request, 'home/index.html', {'message': msg})


