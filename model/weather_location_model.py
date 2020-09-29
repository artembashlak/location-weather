import datetime
import logging

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Float, DateTime

db = SQLAlchemy()

logger = logging.getLogger('sqlalchemy')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class WeatherModel(db.Model):
    __tablename__ = 'weather'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column('city', String(200))
    feels_like = db.Column('feels_like', Float())
    humidity = db.Column('humidity', Float())
    pressure = db.Column('pressure', Float())
    temp = db.Column('temp', Float())
    temp_max = db.Column('temp_max', Float())
    temp_min = db.Column('temp_min', Float())
    time = db.Column(DateTime, default=datetime.datetime.utcnow())
