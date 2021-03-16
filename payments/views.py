from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse


def home(request):
    return render(request, 'payments/home.html')


def signup(request):
    if request.method == 'POST':
        _ = User.objects.create_user(username=request.POST['email'], password=request.POST['password'])
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'payments/signup.html')


def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user:
            login(user)

        return HttpResponse('Invalid credentials')

    return render(request, 'payments/login.html')