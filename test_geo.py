import pytest
import allure
from geo import search, reverse_search
from data import list_place, list_geo


@pytest.mark.parametrize("place, coordinates", list_place)
@allure.story("Проверка поиск координат по названию")
def test_search(place, coordinates):
    with allure.step(f"Поиск координат для '{place}'"):
        result = search(place)
        allure.attach(f"Ожидаемые: {coordinates}, \nПолученные: {result}", name="Результат", attachment_type=allure.attachment_type.TEXT)
        assert search(place) == coordinates


@pytest.mark.parametrize("lat, lon, place", list_geo)
@allure.story("Проверка поиска места по координатам")
def test_reverse_search(lat, lon, place):
    with allure.step(f"Поиск места по координатам ({lat}, {lon})"):
        result = reverse_search(lat, lon)
        allure.attach(f"Ожидаемые: {place}, \nПолученные: {result}", name="Результат", attachment_type=allure.attachment_type.TEXT)
        assert reverse_search(lat, lon) == place
