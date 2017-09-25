# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Article
from django.contrib.auth.models import User

# Create your views here..


def index(request):
    articles = Article.objects.all()
    content = {
        'articles': articles
    }
    for a in articles:
        print(a)
    return render(request, 'articles.html', content)


def register(request):
    errors = []
    formdata = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors.append("Введите имя пользователя")
        elif len(username) < 5:
            errors.append("Имя пользователя должно содержать не менее 5 символов")

        email = request.POST.get('email')
        if not email:
            errors.append("Введите адрес эл. почты")

        firstname = request.POST.get('firstname')
        if not firstname:
            errors.append("Введите своё имя")
        else:
            formdata['firstname'] = firstname

        lastname = request.POST.get('lastname')
        if not lastname:
            errors.append("Введите своё фамилию")
        else:
            formdata['lastname'] = lastname

        password = request.POST.get('password')
        if not password:
            errors.append("Введите пароль")
        elif len(password) < 8:
            errors.append("Пароль должен содержать не менее 8 символов")
        else:
            confirmpass = request.POST.get('confirmpass')
            if not confirmpass:
                errors.append("Подтвердите пароль")
            elif password != confirmpass:
                errors.append("Пароли не совпадают")
                formdata['confirmpass'] = confirmpass
            formdata['password'] = password

        sameusers = []
        try:
            sameusers.append(User.objects.get(username=username))
        except User.DoesNotExist:
            formdata['username'] = username
        try:
            sameusers.append(User.objects.get(email=email))
        except User.DoesNotExist:
            formdata['email'] = email

        if sameusers:
            errors.append("Пользователь с таким именем или адресом эл. почты уже существует")

        if errors:
            return render(request, 'register.html', {'errors': errors, 'formdata': formdata})

        User.objects.create_user(username=username, email=email, password=password)
        return HttpResponseRedirect("/login/")

    return render(request, 'register.html', {'errors': [], 'formdata': formdata})


def login(request):

    return render(request, 'login.html')


def article(request, id):
    art = Article.objects.get(id=int(id))
    content = {
        'article' : art
    }
    return render(request, 'single.html', content)