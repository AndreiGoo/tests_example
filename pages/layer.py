import allure
from selenium.webdriver.common.by import By

from pages.base import BasePageObject


class Layer(BasePageObject):
    """Класс-посредник, хранящий шаблоны локаторов и общие методы для страниц."""

    """Шаблоны локаторов для web-тестов."""
    input_field = "//label[text()='{}']/..//input"
    link_by_text = "//a[text()='{}']"
    link_with_span_text = "//span[text()='{}']/.."
    link_with_contains_class = "//span[contains(@class, '{}')]"
    button_by_text = "//button[text()='{}']"
    element_by_id = "//*[@id='{}']"
    div_by_data_id = "//div[@data-id='{}']"
    div_by_contains_class = "//div[contains(@class, '{}')]"
    div_by_text = "//div[text()='{}']"
    div_by_class = "//div[@class='{}']"

    """Шаблоны локаторов для тестов мобильного приложения."""
    any_by_text = "//*[@text='{}']"
    units_from = "//*[contains(@resource-id, 'radio_group_from')]/*[@text='{}']"
    units_to = "//*[contains(@resource-id, 'radio_group_to')]/*[@text='{}']"
    header_value_from = "//*[contains(@resource-id, 'header_value_from')]"
    header_value_to = "//*[contains(@resource-id, 'header_value_to')]"
    android_button = "//*[@content-desc='{}']"
    calculator_button = "//*[@class='android.widget.Button'][@text='{}']"
    android_error_message = "//*[@class='android.widget.Toast'][@text='{}']"

    @allure.step("Вводит текст в поле ввода по текстовому значению.")
    def send_keys_by_text(self, input_text: str, value: str) -> None:
        """
        Вводит текст в поле ввода по текстовому значению.

        :param input_text: Текстовое значение поля ввода.
        :param value: Вводимый текст.
        """
        locator = self.input_field.format(input_text)
        self.send_keys(By.XPATH, locator, value)

    def click_link_by_text(self, *links: str) -> None:
        """
        Кликает на ссылки по текстовым значениям.

        :param links: Текстовые значения ссылок.
        """
        for link_text in links:
            self.click(By.XPATH, self.link_by_text.format(link_text))

    def click_android_button(self, *buttons_list: str) -> None:
        """
        Кликает на кнопки в мобильном приложении.

        :param buttons_list: Список кнопок.
        """
        for button in buttons_list:
            self.click(By.XPATH, self.android_button.format(button))

    @allure.step("Проверить видимость сообщения об ошибке")
    def check_error_message(self, *error_messages: str) -> bool:
        """
        Проверяет видимость на экране переданных сообщений об ошибках.
        Возвращает True, если сообщения видны.
        Возвращает False, если сообщения не видны.

        :param error_messages: Переданные сообщения об ошибках.
        """
        for error_message in error_messages:
            if not self.wait_visibility(By.XPATH, self.div_by_text.format(error_message)).is_displayed():
                return False
        return True

    @allure.step("Выбрать категорию")
    def choose_category(self, category: str) -> None:
        """
        Выбирает категорию на странице приложения.

        :param category: Название категории.
        """
        self.click(By.XPATH, self.any_by_text.format(category))
