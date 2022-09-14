from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "main/index.html")


def ug_course(request):
    return render(request, "main/ug.html")


def pg_course(request):
    return render(request, "main/pg.html")

def gallery(request):
    return render(request, "main/gallery.html")


def faculty(request):
    return render(request, "main/faculty.html")

def contact(request):
    return render(request, "main/contact.html")


def about_uni(request):
    return render(request, "main/about_uni.html")

def about_clg(request):
    return render(request, "main/about_clg.html")

def about_dev(request):
    return render(request, "main/about_dev.html")