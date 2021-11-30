from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city'] # Form Name is city
        api_req = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+ '&APPID=69969a36adb8fa4aceda4dbddde3abb9').read()
        json_data = json.loads(api_req)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temperature": str(json_data['main']['temp']) + 'k',
            "humidity" : str(json_data['main']['humidity'])
        }
    else:
        city = ''
        data = {}        
    return render(request, 'index.html', {'city':city, 'data':data})