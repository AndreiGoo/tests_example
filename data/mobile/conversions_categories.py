from dataclasses import dataclass


@dataclass
class ConversionsText:
    """Класс, хранящий текстовые значения элементов со страницы "Conversions"."""

    temperature: str = "Temperature"
