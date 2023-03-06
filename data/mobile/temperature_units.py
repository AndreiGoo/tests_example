from dataclasses import dataclass


@dataclass
class TemperatureUnits:
    """Класс, хранящий названия единиц измерения температуры."""

    celsius: str = "Celsius"
    fahrenheit: str = "Fahrenheit"
