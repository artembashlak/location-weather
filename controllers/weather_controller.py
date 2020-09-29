import json

from flask import Blueprint

from services.forecast_service import ForecastService

weather_page = Blueprint('weather_page', __name__)


@weather_page.route('/')
def weather_by_location():
    # return {"name": "Kharkiv",
    #         "feels_like": 10.72,
    #         "humidity": 36,
    #         "pressure": 1019,
    #         "temp": 17.89,
    #         "temp_max": 18,
    #         "temp_min": 17.78}

    return json.dumps(ForecastService.get_forecast().__dict__)
