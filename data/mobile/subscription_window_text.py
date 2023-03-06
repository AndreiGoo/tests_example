from dataclasses import dataclass


@dataclass
class SubscriptionWindowText:
    """Класс, хранящий текстовые значения элементов рекламного окна премиальной подписки."""

    check_box: str = "Never ask again"
    cancel_button: str = "CANCEL"
