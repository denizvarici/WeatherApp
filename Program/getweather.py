import http.client
import apikey
import json

def get_daily_weather(city_name):
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': f"{apikey.api_key}"
        }

    conn.request("GET", f"/weather/getWeather?data.lang=tr&data.city={city_name}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    parsed_data = json.loads(data.decode("utf-8"))

    success = parsed_data.get("success")
    # city = parsed_data.get("city")
    # weather_results = parsed_data.get("result", [])
    # date = weather_results[0].get("date")

    if(success):
        print("fonksiyon başarıyla döndürüldü!")
        return parsed_data

