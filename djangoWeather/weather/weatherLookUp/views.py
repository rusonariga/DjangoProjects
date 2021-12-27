from django.shortcuts import render


def home(request):
    import json
    import requests

    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=B8592975-548D-4B85-810D-805A201A5F4E")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error loading API data from website"

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
