from flask_sqlalchemy import SQLAlchemy

from model.weather_location_model import WeatherModel

db = SQLAlchemy()


class WeatherDAO:
    @staticmethod
    def save(weather_model: WeatherModel):
        db.session.add(weather_model)
        db.session.commit()
        print(weather_model)
