class Converting:
    """Класс, предоставляющий методы для преобразования одних единиц измерения в другие."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Преобразует значение температуры из цельсия в фаренгейты.

        :param celsius: Значение температуры в цельсиях.
        """
        return round(celsius * 1.8 + 32, 4)
