import requests


class LocationService:
    @staticmethod
    def get_city_name():
        city_url = 'http://ipinfo.io/city'
        response_city = requests.get(city_url)
        city_name = ''.join(response_city.content.decode('utf-8').splitlines())
        return city_name
