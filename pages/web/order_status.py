import allure
from selenium.webdriver.common.by import By

from pages.layer import Layer
from data.web.orders import OrdersText


class OrderStatus(Layer):
    """Класс, предоставляющий методы для работы со страницей "Узнать статус заказа". """

    @allure.step('Нажать кнопку "Показать".')
    def show_order_status(self) -> None:
        """
        Нажимает кнопку "Показать".
        """
        self.click(By.XPATH, self.div_by_text.format(OrdersText.show_button))
