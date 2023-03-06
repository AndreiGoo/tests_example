from dataclasses import dataclass


@dataclass
class LoginWindow:
    """Класс, хранящий текстовые значения элементов модального окна входа."""

    error_message: str = "Заполните поле"
