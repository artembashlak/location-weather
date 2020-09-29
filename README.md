Project with Flask and SQLAlchemy

1. Get location by ip
2. Get weather by city name
3. Show json by route /
4. Store data to sql db

Run:

1. pip install -r requirements.txt
2. create .env file with API_KEY_WEATHER
3. python3 app.py

Run in docker:

1. docker build -t weather .
2. docker run -p 5000:5000 weather
3. open http://0.0.0.0:5000/ to get weather