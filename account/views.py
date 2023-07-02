from django.shortcuts import render


def login(request):
    context = {"title": "Login"}
    return render(request, "account/login.html", context=context)
