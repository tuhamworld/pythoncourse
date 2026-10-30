import requests

city = 'Abeokuta'
url = "http://api.weatherapi.com/v1/current.json?key=b6e004ebd88542caab2133546262710&q="+city+"&aqi=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')
country = weather_json.get('location').get('country')

print("Today's weather in", city, country, "is", description, 'and', temp, 'degrees')
