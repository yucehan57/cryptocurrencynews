from django.shortcuts import render

import requests
import json


def home(request):
    """Function-based home view"""

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


def prices(request):
    """Get the price quote using the search button"""
    if request.method == 'POST':
        """pass in 'quote' from search bar name in price.html"""
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,EUR,TRY")
        crypto = json.loads(crypto_request.content)
        context = {
            'quote': quote,
            'crypto': crypto,
        }
        return render(request, 'prices.html', context)
    else:
        notfound = 'Ticker for Crypto currency is not recognized. Please choose a valid three-letter ticker such as XRP for Ripple'
        return render(request, 'prices.html', {
                                        'notfound': notfound,
                                              })
