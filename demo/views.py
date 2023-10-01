from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(["GET"])
def regions_view(request):
    return render(request, "demo/regions.html")


@api_view(["GET"])
def login_view(request):
    return render(request, "demo/auth/login.html")
