import pytest
import allure
from geo import search, reverse_search
from data import list_place, list_geo
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG, filename=f"logs/test_geo.log",
    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
    datefmt='%d/%m/%Y %I:%M:%S', filemode="w"
    )


@pytest.mark.parametrize("place, coordinates", list_place)
@allure.story("Проверка поиск координат по названию")
def test_search(place, coordinates):
    with allure.step(f"Поиск координат для '{place}'"):
        logger.info(f"Ожидаемый результат: {place}")
        result = search(place)
        allure.attach(f"Ожидаемые: {coordinates}, \nПолученные: {result}", name="Результат", attachment_type=allure.attachment_type.TEXT)
        assert search(place) == coordinates
logger.info("Тест прошел успешно!")

@pytest.mark.parametrize("lat, lon, place", list_geo)
@allure.story("Проверка поиска места по координатам")
def test_reverse_search(lat, lon, place):
    with allure.step(f"Поиск места по координатам ({lat}, {lon})"):
        logger.info(f"Ожидаемый результат: {lat}, {lon}")
        result = reverse_search(lat, lon)
        allure.attach(f"Ожидаемые: {place}, \nПолученные: {result}", name="Результат", attachment_type=allure.attachment_type.TEXT)
        assert reverse_search(lat, lon) == place
logger.info("Тест прошел успешно!")
