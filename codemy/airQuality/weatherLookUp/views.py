from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == 'POST':
        zipCode = request.POST['zipCode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipCode + "&distance=25&API_KEY=B8592975-548D-4B85-810D-805A201A5F4E")
        print(f"zipCode:{zipCode}")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error loading API data from website"

        if api[0]['Category']['Number'] == 1:
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Number'] == 2:
            category_description = "(51-100) Air quality is accetable; however, for some pollutants there may be a moderate heath concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Number'] == 3:
            category_description = "(101-150) Ahtough general public is not likely to be affected at this AQI range, people with lung desease, older adults and chidren area at greater risk from exposure to ozone, whereas persons with hearth and lung desease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "usg"
        elif api[0]['Category']['Number'] == 4:
            category_description = "(151-200) Everyone may begin to expredience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Number'] == 5:
            category_description = "(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryUnhealthy"
        elif api[0]['Category']['Number'] == 6:
            category_description = "(301-500) health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color})

    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=B8592975-548D-4B85-810D-805A201A5F4E")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error loading API data from website"

        if api[0]['Category']['Number'] == 1:
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Number'] == 2:
            category_description = "(51-100) Air quality is accetable; however, for some pollutants there may be a moderate heath concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Number'] == 3:
            category_description = "(101-150) Ahtough general public is not likely to be affected at this AQI range, people with lung desease, older adults and chidren area at greater risk from exposure to ozone, whereas persons with hearth and lung desease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "usg"
        elif api[0]['Category']['Number'] == 4:
            category_description = "(151-200) Everyone may begin to expredience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Number'] == 5:
            category_description = "(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryUnhealthy"
        elif api[0]['Category']['Number'] == 6:
            category_description = "(301-500) health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
