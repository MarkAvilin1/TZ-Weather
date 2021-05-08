import requests
from datetime import datetime

"""Get weather information from the API of https://openweathermap.org"""


class WeatherData:
    KEY = "aba9c361e3bf4c76f293a9bfdf535be7"
    API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"

    def __init__(self, lat, lon):
        self.parameters = {
            "lat": lat,
            "lon": lon,
            "appid": self.KEY,
            "exclude": "minutely,hourly,alerts",
            "units": "metric"
        }
        self.response = requests.get(url=self.API_ENDPOINT, params=self.parameters)
        self.response.raise_for_status()
        self.response.status_code
        self.data = self.response.json()
        self.days = self.data['daily'][:5]
        self.max_press = self.max_press()
        self.min_temp = self.min_temp()
        self.city = self.data["timezone"].split('/')[1]
        self.current = self.data['current']
        self.date = datetime.fromtimestamp(self.current['dt']).strftime('%d.%m.%Y')
        self.sunrise = datetime.fromtimestamp(self.current['sunrise']).strftime('%H:%M:%S')
        self.sunset = datetime.fromtimestamp(self.current['sunset']).strftime('%H:%M:%S')
        self.temp = self.current['temp']
        self.feels_like = self.current['feels_like']
        self.pressure = self.current['pressure']
        self.humidity = self.current['humidity']
        self.wind_speed = self.current['wind_speed']

    def max_press(self):
        pressures = []
        for day in self.days:
            pressures.append(int(day['pressure']))
        max_index = int(pressures.index(max(pressures)))
        dt = self.days[max_index]['dt']
        date = datetime.fromtimestamp(dt).strftime('%d.%m.%Y')
        return f'''
        {date} максимальное давление за 5 дней "{max(pressures)} мбар"'''

    def min_temp(self):
        temps = []
        dt: int
        for day in self.days:
            def_temp = day['temp']['night'] - day['temp']['morn']
            temps.append(float(def_temp))
        min_index = int(temps.index(min(temps)))
        dt = self.days[min_index]['dt']
        date = datetime.fromtimestamp(dt).strftime('%d.%m.%Y')
        return f'''
        {date} самая минимальная разница температуры "{round(min(temps), 2)} °C"'''
