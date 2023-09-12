import requests

parameters = {
    'lat': 39.048953,
    'lon': -76.688273,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily',
}

res = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
res.raise_for_status()
data = res.json()
weather_slice = data['hourly'][:13]

rain = False

for hour_data in weather_slice:
    weather_code = hour_data['weather'][0]['id']
    if weather_code < 700:
        rain = True
if rain:
    print("Bring Umbrella")
