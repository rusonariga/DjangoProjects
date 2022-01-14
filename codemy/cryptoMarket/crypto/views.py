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


def prices(request):
    import requests
    import json
    if request.method == 'POST':
        # name into the request should be the same that input was called at html
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)

        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        return render(request, 'prices.html', {})
