from dataclasses import dataclass


@dataclass
class ItemsText:
    """Класс, хранящий текст кнопки на товаре."""

    buy_button: str = "Купить"
    changed_button: str = "В корзине"
