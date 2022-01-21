from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'authenticate/home.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Succesfully logged in"))
            return redirect('home')
        else:
            messages.error(
                request, ("Error loggin in - please check your inputs"))
            return redirect('user_login')
    else:
        return render(request, 'authenticate/login.html', {})


def user_logout(request):
    logout(request)
    messages.success(request, ("Succesfully logged out"))
    return redirect('home')
