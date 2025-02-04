import requests

url_base = "https://nominatim.openstreetmap.org/"
headers = {'User-Agent': 'MyGeocodingApp/1.0 (myemail@example.com)'}

def search(city):
    url = f"{url_base}search?q={city}&format=json"
    response = requests.get(url, headers=headers)
    data = response.json()
    if data:
        lat = data[0]['lat']
        lon = data[0]['lon']
        final = f"Широта: {lat}, Долгота: {lon}"
        return final
    else:
        return "Город не найден"

def reverse_search(lat, lon):
    url = f"{url_base}reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=0&dedupe=0"
    response = requests.get(url, headers=headers)
    data = response.json()
    if "error" in data:
        return ("Город не найден.")
    else:
        return data["display_name"]
