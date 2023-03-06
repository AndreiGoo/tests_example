import allure

from api_helper.search import Search


@allure.title("Поиск товаров по названию")
@allure.severity("Normal")
def test_get_presearch():
    assert Search().check_presearch(), "Некорректный поиск товаров по названию."
