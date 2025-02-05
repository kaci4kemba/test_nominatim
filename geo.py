import requests
import logging

logger = logging.getLogger(__name__)

url_base = "https://nominatim.openstreetmap.org/"
headers = {'User-Agent': 'MyGeocodingApp/1.0 (myemail@example.com)'}


def search(place):
    logger.info(f"Составляем url для запроса используя {url_base} и {place}")
    url = f"{url_base}search?q={place}&format=json"
    response = requests.get(url, headers=headers)
    logger.info(f"Получаем ответ: {response.json()}")
    data = response.json()
    if data:
        logger.info(f"Вытаскиваем координаты из {data}")
        lat = data[0]['lat']
        lon = data[0]['lon']
        final = f"Широта: {lat}, Долгота: {lon}"
        logger.info(f"Возвращаем полученные координаты: {final}")
        return final
    else:
        logger.info(f"По переданным данным ничего не нашли")
        return "Город не найден"

def reverse_search(lat, lon):
    logger.info(f"Составляем url для запроса используя {url_base}, {lat} и {lon}")
    url = f"{url_base}reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=0&dedupe=0"
    response = requests.get(url, headers=headers)
    logger.info(f"Получаем ответ: {response.json}")
    data = response.json()
    if "error" in data:
        logger.info(f"По переданным координатам ничего не нашли")
        return "Город не найден"
    else:
        logger.info(f"Возвращаем полученную информацию о месте: {data['display_name']}")
        return data["display_name"]
