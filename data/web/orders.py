from dataclasses import dataclass


@dataclass
class OrdersText:
    """Класс, хранящий текстовые значения элементов со страницы "Узнать статус заказа"."""

    phone: str = "Телефон"
    order_number: str = "Номер заказа"
    show_button: str = "Показать"

    error_message_phone: str = "Телефон указан неверно"
    error_message_number: str = "Номер заказа указан неверно"

    invalid_phone_value: str = "5555555555"
    invalid_order_number_value: str = "gggggggggg"
