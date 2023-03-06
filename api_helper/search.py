import allure

from api_helper.base import BaseRequest
from data.web.test_data import Routes


class Search(BaseRequest):
    """Класс, предоставляющий методы для поиска."""

    @allure.step('Выполнить get-запрос поиска товаров по названию.')
    def get_presearch(self) -> dict:
        """
        Выполняет get-запрос поиска товара под названием "iphone", затем возвращает результат поиска.
        """
        url = Routes.base_api + Routes.get_presearch
        payload = {'query': 'iphone'}
        response = self.get(url, payload)
        return self.loads(response.text)

    @allure.step('Проверить результаты поиска.')
    def check_presearch(self) -> bool:
        """
        Проверяет, что результат поиска содержит имя искомого товара.
        """
        for dictionary in self.get_presearch()["data"]["suggests"]:
            if "iphone" not in dictionary["query"]:
                return False
        return True
