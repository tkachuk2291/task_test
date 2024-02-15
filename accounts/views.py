from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login


# Определяем представление для страницы входа
def login_view(request: HttpRequest) -> HttpResponse:
    # Проверяем, был ли запрос методом GET
    if request.method == "GET":
        # Если да, отображаем страницу входа
        return render(request, "accounts/login.html")
    # Проверяем, был ли запрос методом POST
    elif request.method == "POST":
        # Если да, получаем значения, введенные пользователем в форму входа
        username = request.POST["username"]
        password = request.POST["password"]
        # Аутентифицируем пользователя с использованием введенных им учетных данных
        user = authenticate(username=username, password=password)
        # Проверяем, была ли успешной аутентификация пользователя
        if user:
            # Если да, выполняем вход пользователя
            login(request, user)
            # Перенаправляем пользователя на главную страницу
            return HttpResponseRedirect(reverse("catalog:index"))
        else:
            # Если аутентификация не удалась, формируем контекст с сообщением об ошибке
            error_context = {"error": "Invalid credentials"}
            # Отображаем страницу входа с сообщением об ошибке
            return render(request, "accounts/login.html", context=error_context)
