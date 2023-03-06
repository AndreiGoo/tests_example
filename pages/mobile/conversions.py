import allure
from selenium.webdriver.common.by import By

from pages.layer import Layer
from mobile_helper.converting import Converting
from mobile_helper.buttons_names import ButtonsNames


class Conversions(Layer):
    """Класс, предоставляющий методы для работы со страницей "Conversions"."""

    @allure.step("Выбрать единицу измерения, из которой надо преобразовать значение величины.")
    def choose_unit_from(self, unit: str) -> None:
        """
        Выбирает единицу измерения, из которой надо преобразовать значение величины.

        :param unit: Название единицы измерения.
        """
        self.click(By.XPATH, self.units_from.format(unit))

    @allure.step("Выбрать единицу измерения, к которой надо преобразовать значение величины.")
    def choose_unit_to(self, unit: str) -> None:
        """
        Выбирает единицу измерения, к которой надо преобразовать значение величины.

        :param unit: Название единицы измерения.
        """
        self.click(By.XPATH, self.units_to.format(unit))

    @allure.step("Проверить преобразование значений температуры из цельсия в фаренгейты.")
    def check_celsius_to_fahrenheit_conversion(self, temperature_values: list) -> bool:
        """
        Проверяет преобразование значений температуры из цельсия в фаренгейты.

        :param temperature_values: Список значений температуры в цельсиях.
        """
        self.click_android_button(ButtonsNames.clear_button)
        for celsius in temperature_values:
            self.send_keys(By.XPATH, self.header_value_from, celsius)
            fahrenheit_from_formula = Converting.celsius_to_fahrenheit(celsius)
            fahrenheit_from_app = \
                float(self.get_element_attribute(self.wait_located(By.XPATH, self.header_value_to), "text"))
            if not fahrenheit_from_formula == fahrenheit_from_app:
                return False
            self.click_android_button(ButtonsNames.clear_button)
        return True
