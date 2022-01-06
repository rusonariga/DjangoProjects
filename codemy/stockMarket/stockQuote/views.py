from django.shortcuts import redirect, render
from .models import stock
from django.contrib import messages
from .forms import stockForm


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker_input']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_9c23b434f75d428eb7753d06ca042844")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "enter a ticker symbol please"})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):

    if request.method == 'POST':

        form = stockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(
                request, ("stock has been added to your portfolio"))
            return redirect('add_stock')
        # else:

    else:
        ticker = stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': ticker})
