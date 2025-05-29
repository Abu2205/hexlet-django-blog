# hexlet_django_blog/views.py
from django.shortcuts import render

def about(request):
    return render(
        request,
        "about.html",
        context={
            "who": "World",
        },
    )

def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "World",
        },
    )

def index(request):
    context = {
        'app_name': 'Article'
    }
    return render(request, "articles/index.html", context)