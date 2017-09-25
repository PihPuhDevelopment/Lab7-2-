# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Article
from django.contrib.auth.models import User
import forms

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
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            username = form.username
            email = form.email
            firstname = form.firstname
            lastname = form.lastname
            password = form.password
            confirmpass = form.confirmpass

            formdata['firstname'] = firstname
            formdata['lastname'] = lastname
            formdata['password'] = password

            if password != confirmpass:
                errors.append("Пароли не совпадают")

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