from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9d5c397799e874739b747e8fe09e58a6').read()
        json_data = json.loads(res)
        context = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+ ' ' +
            str(json_data['coord']['lat']),
            "temp": int(json_data['main']['temp']) - 273,
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ''
        context = {}

    return render(request, 'index.html' , {'city':city, 'context':context})