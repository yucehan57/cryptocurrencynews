from django.shortcuts import render

# Create your views here.

def home(request):
    """Function-based home view"""
    import requests
    import json


    # grab currency trade price
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD,EUR,TRY")
    price = json.loads(price_request.content)



    # grab crpyto currency news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    # pass the data
    context = {
        'api': api,
        'price': price,
    }
    return render(request, 'home.html', context)
