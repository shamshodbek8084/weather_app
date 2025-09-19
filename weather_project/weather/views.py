from django.shortcuts import render
from django.views import View
import requests

class WeatherView(View):
    template_name = 'weather/home.html'

    def get(self, request):
        city = request.GET.get('city')
        weather_data = None

        if city:
            api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"
            response = requests.get(url).json()

            if response.get("cod") == 200:
                weather_data = {
                    'city': city,
                    'temperature': response['main']['temp'],
                    'description': response['weather'][0]['description'],
                    'icon': response['weather'][0]['icon'],
                }
            else:
                weather_data = {'error': "City not found!"}

        return render(request, self.template_name, {'weather': weather_data})
