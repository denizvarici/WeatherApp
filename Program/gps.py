import requests

def get_location_by_ip():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    city = data.get('city')
    print(data)
    print(f'Bulunduğunuz şehir: {city}')

get_location_by_ip()