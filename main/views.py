from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "main/index.html")


def ug_course(request):
    return render(request, "main/ug.html")


def pg_course(request):
    return render(request, "main/pg.html")