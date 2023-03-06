import allure
from selenium.webdriver.common.by import By

from pages.layer import Layer


class MainPage(Layer):
    """Класс, предоставляющий методы для работы с главной страницей."""

    @allure.step("Навести курсор мыши на значок входа.")
    def mouseover_login_menu(self) -> None:
        """
        Наводит курсор на значок "Войти".
        """
        login_menu = self.wait_visibility(By.XPATH, self.div_by_class.format("user-profile__login"))
        self.mouseover(login_menu)

    @allure.step('Нажать кнопку "Войти".')
    def press_login_button(self) -> None:
        """
        Нажимает кнопку "Войти" в выпадающем окне входа.
        """
        self.click(By.XPATH, '//div[@class="user-profile__wrapper"]//span[text()="Войти"]')

    @allure.step("Ввести пустое поле.")
    def send_empty_field(self) -> None:
        """
        Вводит пустое значение в поле ввода.
        """
        self.press_enter(By.XPATH, self.input_field.format("Телефон или e-mail"))
