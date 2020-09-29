import flask

from controllers.weather_controller import weather_page
from model.weather_location_model import db

app = flask.Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db.app = app
db.init_app(app)
db.create_all()
app.register_blueprint(weather_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
