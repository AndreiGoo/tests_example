from selenium.webdriver.common.by import By

from pages.layer import Layer


class Categories(Layer):
    """Класс, предоставляющий методы для работы со страницей, содержащей категории товаров."""

    def choose_categories(self, *categories: str) -> None:
        """
        Выбирает категории товаров по текстовым значениям.

        :param categories: Текстовые значения категорий товаров.
        """
        for category in categories:
            self.click(By.XPATH, self.link_with_span_text.format(category))

