import requests
import logging

logger = logging.getLogger(__name__)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


def search(place):
    logger.info(f"Составляем url для запроса используя {place}")
    url = f"https://nominatim.openstreetmap.org/search?q={place}&format=json"
    logger.info(f"Отправляем запрос с {url}")
    response = requests.get(url, headers=headers)
    logger.info(f"Проверка успешности запроса (200)")
    if response.status_code != 200:
        logger.info(f"Статус-код пришел отличный({response.status_code}) от ожидаемого (200)")
        return "Ошибка при запросе"
    logger.info(f"Парсим json из ответа в переменную data")
    data = response.json()
    logger.info(f"Проверяем что {data} не пуст")
    if data:
        logger.info(f"Вытаскиваем координаты из {data}")
        lat = data[0]['lat']
        lon = data[0]['lon']
        logger.info(f"Присваиваем координаты переменной")
        final = lat, lon
        logger.info(f"Возвращаем полученные координаты: {final}")
        return final
    else:
        logger.info(f"По переданным данным ничего не нашли")
        return "Город не найден"


def reverse_search(lat, lon):
    logger.info(f"Составляем url для запроса используя {lat} и {lon}")
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=0&dedupe=0"
    logger.info(f"Отправляем запрос с {url}")
    response = requests.get(url, headers=headers)
    logger.info(f"Проверка успешности запроса (200)")
    if response.status_code != 200:
        logger.info(f"Статус-код пришел отличный({response.status_code}) от ожидаемого (200)")
        return "Ошибка при запросе"
    logger.info(f"Парсим json из ответа в переменную data")
    data = response.json()
    logger.info(f"Проверяем {data} на ошибки")
    if "error" in data:
        logger.info(f"По переданным координатам ничего не нашли")
        return "Город не найден"
    else:
        logger.info(f"Возвращаем полученную информацию о месте: {data['display_name']}")
        return data["display_name"]
