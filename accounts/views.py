from typing import Type

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("catalog:index"))
        else:
            context = {
                'login': 'Invalid login or password'
            }
        return render(request, 'registration/login.html', context)


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return render(request, 'registration/logged_out.html')
