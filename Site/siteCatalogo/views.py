from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hey.</h1>'),

def pagina(request):
    return render(request, 'index.html')
