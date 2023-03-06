from dataclasses import dataclass


@dataclass
class MainPageText:
    """Класс, хранящий текстовые значения элементов с главной страницы."""

    buyers: str = "Покупателям "
    status: str = "Узнать статус заказа"
