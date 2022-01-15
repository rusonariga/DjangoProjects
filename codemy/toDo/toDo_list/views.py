from django.shortcuts import render
from .models import List


def home(request):
    task_all = List.objects.all
    return render(request, 'home.html', {'task_all': task_all})


def about(request):
    full_name = {'first_name': 'Kid', 'last_name': 'Rock'}
    return render(request, 'about.html', full_name)
