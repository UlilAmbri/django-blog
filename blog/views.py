from django.shortcuts import render
from .models import Post

def home_view(request):
    context = {}

    post = Post.objects.all()
    context["posts"] = post

    return render(request, "home.html", context)

def about_view(request):
    context = {}
    context["nama"] = "Ulil Ambri"
    context["asal"] = "Pekanbaru"
    context["tinggi"] = "164"
    context["bb"] = "83"

    return render(request, "about.html", context)
