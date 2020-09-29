import os

import requests

from dto.weather_dto import WeatherDTO


class WeatherService:
    @staticmethod
    def get_weather_by_city_name(city_name: str):
        api_key = os.getenv("API_KEY_WEATHER")
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
              city_name + '&appid=' + api_key + '&units=metric'

        response = requests.get(url).json()

        weather_location_dto = WeatherDTO()

        weather_location_dto.name = response['name']
        weather_location_dto.humidity = response['main']['humidity']
        weather_location_dto.feels_like = response['main']['feels_like']
        weather_location_dto.pressure = response['main']['pressure']
        weather_location_dto.temp = response['main']['temp']
        weather_location_dto.temp_max = response['main']['temp_max']
        weather_location_dto.temp_min = response['main']['temp_min']

        return weather_location_dto
