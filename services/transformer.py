from dto.weather_dto import WeatherDTO
from model.weather_location_model import WeatherModel


class Transformer:
    @staticmethod
    def transform_weather_dto_to_weather_model(weather_dto: WeatherDTO):
        weather_model = WeatherModel()
        weather_model.city = weather_dto.name
        weather_model.humidity = weather_dto.humidity
        weather_model.feels_like = weather_dto.feels_like
        weather_model.pressure = weather_dto.pressure
        weather_model.temp_max = weather_dto.temp_max
        weather_model.temp_min = weather_dto.temp_min
        weather_model.temp = weather_dto.temp
        return weather_model
