from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def about(request):
    full_name = {'first_name': 'Kid', 'last_name': 'Rock'}
    return render(request, 'about.html', full_name)
