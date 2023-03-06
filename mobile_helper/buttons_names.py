from dataclasses import dataclass


@dataclass
class ButtonsNames:
    """Класс, хранящий имена кнопок приложения."""

    clear_button: str = "Clear Value"
