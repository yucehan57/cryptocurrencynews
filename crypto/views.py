from django.shortcuts import render

# Create your views here.

def home(request):
    """Function-based home view"""
    import requests
    import json
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    context = {
        'api': api
    }
    return render(request, 'home.html', context)
