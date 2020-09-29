from dao.weather_dao import WeatherDAO
from services.location_service import LocationService
from services.transformer import Transformer
from services.weather_service import WeatherService


class ForecastService:
    @staticmethod
    def get_forecast():
        city_name = LocationService.get_city_name()
        weather_dto = WeatherService.get_weather_by_city_name(city_name)
        weather = Transformer.transform_weather_dto_to_weather_model(weather_dto)
        WeatherDAO.save(weather)
        return weather_dto
