import pytest
import allure
from geo import search, reverse_search
from data_extractor import get_test_data


@allure.story("Проверка поиска координат по названию")
@pytest.mark.parametrize("test_data", (get_test_data()))
def test_search(test_data):
    with allure.step("Подготовка переменных"):
        place = test_data["display_name"]
        coordinates = (test_data["lat"], test_data["lon"])
    with allure.step(f"Поиск координат для '{place}'"):
        result = search(place)
    with allure.step("Проверка на корректность"):
        assert result == coordinates, "Некорректные данные"


@pytest.mark.parametrize("test_data", (get_test_data()))
@allure.story("Проверка поиска места по координатам")
def test_reverse_search(test_data):
    with allure.step("Подготовка переменных"):
        lat, lon = (test_data["lat"], test_data["lon"])
        place = test_data["display_name"]
    with allure.step(f"Поиск места по координатам {lat} и {lon}"):
        result = reverse_search(lat, lon)
    with allure.step("Проверка на корректность"):
        assert result == place
