from django.shortcuts import render


def home(request):
    import requests
    import json

    # Crypto data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETC,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    # Crypto news
    news_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = json.loads(news_request.content)

    return render(request, 'home.html', {'news': news, 'price': price})
