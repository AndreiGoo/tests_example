import allure
from selenium.webdriver.common.by import By

from pages.layer import Layer

from data.web.items import ItemsText
from data.web.test_data import Routes


class ItemsList(Layer):
    """Класс, предоставляющий методы для работы со страницей, содержащей список товаров."""

    @allure.step('Нажать кнопку "Купить" у первого товара в списке.')
    def buy_first_item(self) -> None:
        """
        Покупает первый товар в списке.
        """
        self.click(By.XPATH, self.button_by_text.format(ItemsText.buy_button))

    @allure.step("Проверить видимость модального окна, сообщающего о добавлении товара в корзину.")
    def check_modal_window_displayed(self) -> bool:
        """
        Проверяет видимость модального окна, сообщающего о добавлении товара в корзину.
        Возвращает True, если окно видно.
        Возвращает False, если окно не видно.
        """
        return self.wait_visibility(By.XPATH, self.element_by_id.format("app-cart-modal")).is_displayed()

    @allure.step("Получить код товара, который первый в списке.")
    def get_first_item_code_list(self) -> str:
        """
        Возвращает код товара, который первый в списке.
        """
        element = self.wait_located(By.XPATH, self.div_by_data_id.format("product"))
        return self.get_element_attribute(element, "data-code")

    @allure.step("Получить код товара, который первый в корзине.")
    def get_first_item_code_cart(self) -> str:
        """
        Возвращает код товара, который первый в корзине.
        """
        element = self.wait_located(By.XPATH, self.div_by_contains_class.format("product-code"))
        return element.text

    @allure.step('Проверить, что надпись на кнопке "Купить" после нажатия изменилась на "В корзине".')
    def check_button_text_changes(self) -> bool:
        """
        Проверяет, что надпись на кнопке "Купить" после нажатия изменилась на "В корзине".
        Возвращает True, если надпись изменилась.
        Возвращает False, если надпись не изменилась.
        """
        return self.wait_visibility(By.XPATH, self.button_by_text.format(ItemsText.changed_button)).is_displayed()

    @allure.step('Перейти по ссылке "Корзина"')
    def open_cart(self) -> None:
        """
        Открывает корзину с товарами.
        """
        self.click(By.XPATH, self.link_with_contains_class.format("buttons__link-price"))

    @allure.step("Проверить, что адрес корзины соответствует адресу, хранящимся в базе данных.")
    def check_url_cart(self) -> bool:
        """
        Проверяет, что адрес корзины соответствует адресу, хранящимся в базе данных.
        Возвращает True, если соответствует.
        Возвращает False, если не соответствует.
        """
        return self.get_url() == Routes.main_page + Routes.cart
