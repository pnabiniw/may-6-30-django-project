from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def user_login(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(request, username=un, password=pw)
        if user is not None:
            login(request, user)
            return redirect("students")
        else:
            return redirect("login")
    context = {"title": "Login"}
    return render(request, "account/login.html", context=context)


def user_logout(request):
    logout(request)
    return redirect("login")


from django.contrib.auth.models import User
