from django.shortcuts import redirect, render
from .models import stock
from django.contrib import messages
from .forms import stockForm
"""
1: una vez que ya cree una columna en la base de datos, como la elimino o modifico el tag
2: como hacer para cambiar en el add stock de ticker a ticker_add
3: de donde le esta pasando el stock_id? desde el html?
4. Como hacer funcional el boton de delete de la lista
5. Como hacer distintos returns depende de quien llama (no tener 2 delete fucntions).
6. como manejar cuando se apreta el boton buscar y no hay nada
"""


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker_input']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_9c23b434f75d428eb7753d06ca042844")

        try:
            api = json.loads(api_request.content)
            messages.success(request, ("Successfully loaded"))
        except Exception as e:
            api = "Error"
            messages.error(request, ("Not found, check the ticket input"))

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "enter a ticker symbol please"})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    import requests
    import json

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
        api_output = []

        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(
                ticker_item) + "/quote?token=pk_9c23b434f75d428eb7753d06ca042844")
            try:
                api = json.loads(api_request.content)
                api.update({'tickerID': ticker_item.id})
                api_output.append(api)
                messages.success(request, ("Successfully loaded"))
            except Exception as e:
                api = "Error"
                messages.error(request, ("Not found, check the ticket input"))

        return render(request, 'add_stock.html', {'ticker': ticker, 'api_output': api_output})


def delete_stock(request, stock_id):
    item = stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect(add_stock)


def remove_stock(request):
    ticker = stock.objects.all()
    return render(request, 'remove_stock.html', {'ticker': ticker})


def delete_stock2(request, stock_id):
    item = stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect(remove_stock)
