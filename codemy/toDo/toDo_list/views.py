from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
"""

"""


def home(request):

    # navbar button functionality to add item in list
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid() and request.POST['item'] != '':
            form.save()
            task_all = List.objects.all
            messages.success(request, ('The task \'{}\' has been added to the List'.format(
                request.POST['item'])))
            return render(request, 'home.html', {'task_all': task_all})
        else:
            task_all = List.objects.all
            messages.error(
                request, ('Cannot add an empty task, check your input'))
            return render(request, 'home.html', {'task_all': task_all})

    else:
        task_all = List.objects.all
        return render(request, 'home.html', {'task_all': task_all})


def about(request):
    full_name = {'first_name': 'Kid', 'last_name': 'Rock'}
    return render(request, 'about.html', full_name)


def item_delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return redirect('home')


def item_change_status(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = not item.completed
    item.save()
    messages.success(request, ('Item status has been changed'))
    return redirect('home')


def item_edit(request, list_id):
    if request.method == 'POST':
        task = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=task)

        if form.is_valid() and request.POST['item'] != '':
            form.save()
            task_all = List.objects.all
            messages.success(request, ('The task \'{}\' has been edited on   the List'.format(
                request.POST['item'])))
            return redirect('home')

    else:
        task = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'task': task})
