import requests
from json import loads


class BaseRequest:
    """Класс, предоставляющий методы для работы с API."""

    @staticmethod
    def get(url: str, params: dict = None, headers: dict = None): # -> class:`Response <Response>` object
        """
        Выполняет get-запрос, затем возвращает ответ на него.

        :param url: URL-адрес запроса
        :param params: Параметры
        :param headers: Заголовки
        """
        response = requests.get(url=url,
                                params=params,
                                headers=headers)
        return response

    @staticmethod
    def loads(text: str) -> dict:
        """
        Десериализует текст, содержащий документ JSON, в объект Python.

        :param text: Текст, содержащий документ JSON.
        """
        return loads(text)
