from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm


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


def user_registration(request):
    if request.method == 'POST':
        # form_registration = UserCreationForm(request.POST)
        form_registration = SignUpForm(request.POST)
        if form_registration.is_valid():
            form_registration.save()
            username = form_registration.cleaned_data['username']
            password = form_registration.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Succesfully signed up"))
            return redirect('home')
        else:
            messages.error(
                request, ("Error in the form - please check your inputs"))

    else:
        # form_registration = UserCreationForm()
        form_registration = SignUpForm()

    context = {'form_registration': form_registration}
    return render(request, 'authenticate/register.html', context)


def user_profile_edit(request):
    if request.method == 'POST':
        form_registration = EditProfileForm(
            request.POST, instance=request.user)
        if form_registration.is_valid():
            form_registration.save()
            messages.success(request, ("You have edited your profile"))
            return redirect('home')
        else:
            messages.error(
                request, ("Error in the form - please check your inputs"))

    else:
        # instance retrieve info from DB
        form_registration = EditProfileForm(instance=request.user)

    context = {'form_registration': form_registration}
    return render(request, 'authenticate/profile_edit.html', context)


def user_password_update(request):
    if request.method == 'POST':
        form_registration = PasswordChangeForm(
            data=request.POST, user=request.user)
        if form_registration.is_valid():
            form_registration.save()
            # to avoid be logged out when pass is changed
            update_session_auth_hash(request, form_registration.user)
            messages.success(request, ("You have updated your password"))
            return redirect('home')
        else:
            messages.error(
                request, ("Error in the form - please check your inputs"))

    else:
        # instance retrieve info from DB
        form_registration = PasswordChangeForm(user=request.user)

    context = {'form_registration': form_registration}
    return render(request, 'authenticate/password_update.html', context)
