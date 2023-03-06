from selenium.webdriver.common.by import By

from pages.layer import Layer

from data.mobile.subscription_window_text import SubscriptionWindowText


class PremiumSubscriptionWindow(Layer):
    """Класс, предоставляющий методы для работы с рекламным окном премиальной подписки."""

    def close_popup(self) -> None:
        """
        Закрывает всплывающее окно при входе в приложение.
        """
        self.click(By.XPATH, self.any_by_text.format(SubscriptionWindowText.check_box))
        self.click(By.XPATH, self.any_by_text.format(SubscriptionWindowText.cancel_button))
