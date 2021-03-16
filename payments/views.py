from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def home(request):
    return render(request, 'payments/home.html')


def signup(request):
    if request.method == 'POST':
        _ = User.objects.create_user(username=request.POST['email'], password=request.POST['password'])
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'payments/signup.html')