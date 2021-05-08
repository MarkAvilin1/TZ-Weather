from tkinter import *
from weather_data import WeatherData

"""Graphical interface to show the weather details"""
weather = WeatherData(51.485298, 46.126720)

window = Tk()

window.geometry("670x400")
window.title("Weather App")
window.config(padx=50, pady=50, bg="#EFFFFF")

press = Label(text=weather.max_press, bg="#EFFFFF", fg="#040404", font=("Ariel", 12, "bold"))
press.grid(column=0, row=0)

temp = Label(text=weather.min_temp, bg="#EFFFFF", fg="#040404", font=("Ariel", 12, "bold"))
temp.grid(column=0, row=1)

current_city = Label(text=f'''
Город: {weather.city}
Дата: {weather.date}
Восход: {weather.sunrise}
Закат: {weather.sunset}
Температура воздуха: {int(weather.temp)} °C
Реальное ощущение: {int(weather.feels_like)} °C
Давление: {weather.pressure} мбар
Влажность: {weather.humidity} %
Скорость ветра: {weather.wind_speed} м/с
''', bg="#EFFFFF", fg="#040404", font=("Ariel", 12, "bold"), justify="left")
current_city.grid(column=0, row=2)

window.mainloop()





