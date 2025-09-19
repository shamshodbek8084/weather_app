import requests
from django.shortcuts import render
from django.views import View

ICON_MAP = {
    "clear": "☀️",
    "sunny": "☀️",
    "clouds": "☁️",
    "cloudy": "☁️",
    "rain": "🌧️",
    "rainy": "🌧️",
    "snow": "❄️",
    "snowy": "❄️",
    "thunderstorm": "⛈️",
    "storm": "⛈️",
    "mist": "🌫️",
    "fog": "🌫️",
    "haze": "🌫️",
}

def get_weather_icon(condition):
    condition = condition.lower()
    for key, icon in ICON_MAP.items():
        if key in condition:
            return icon
    return "🌤️"  # default


class WeatherView(View):
    def get(self, request):
        weather_data = None
        city = request.GET.get("city")

        if city:
            api_key = "259afab76ef42e09f450458b74b2f279"  # ✅ real API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                description = data["weather"][0]["description"]

                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": description,
                    "feels_like": data["main"]["feels_like"],
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"],
                    "pressure": data["main"]["pressure"],
                    "icon": get_weather_icon(description),
                }
            else:
                weather_data = {"error": "City not found."}

        return render(request, "home.html", {"weather": weather_data})
