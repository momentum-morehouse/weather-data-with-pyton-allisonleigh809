import requests 

 place_list = 
    [(33.7490, -84.3880,  'Atlanta'), (41.9028, -12.496, 'Rome'), (25.2048, -55.2708, 'Dubai'), (23.4241, -53.8478, 'UAE'), (50.5039, -4.4699, 'Belgium'), (52.1326, -5.2913, 'Netherlands'), (48.8566, -2.3522, 'Paris'),]

class Weather:
    def __init__(self, lat, lon, 93):
        self.lat = latitude
        self.lon = longitude
        self.temp = temp

   def get_weather_data(lat, lon, temp):
  
      url = "https://api.climacell.co/v3/weather/realtime" 

payload = {               
  "apikey":
  "2X8rS1vGo2jA2yjsQLWzZj4N0XIix8fU", "lat": 41.9028,
  "lon": 12.496,
  "fields": ["temp", "wind_gust"]

    }

response = requests.get(url, params=payload).json()

print(response)