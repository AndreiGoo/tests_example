from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys


class BasePageObject:
    """Класс, предоставляющий методы для работы с драйвером браузера."""

    def __init__(self, driver):
        self.driver = driver

    def wait_located(self, by: By, locator: str, timeout: int = 10) -> WebElement:
        """
        Ожидает, когда элемент появится в DOM, затем возвращает его.

        :param by: Стратегия поиска.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания в секундах.
        """
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((by, locator)))

    def wait_visibility(self, by: By, locator: str, timeout: int = 10) -> WebElement:
        """
        Ожидает, когда элемент станет видимым на экране, затем возвращает его.

        :param by: Стратегия поиска.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания в секундах.
        """
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((by, locator)))

    def click(self, by: By, locator: str, timeout: int = 10) -> None:
        """
        Ожидает, когда элемент станет кликабельным, затем кликает на него.

        :param by: Стратегия поиска.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((by, locator))).click()

    def send_keys(self, by: By, locator: str, text: str, timeout: int = 10) -> None:
        """
        Ожидает, когда поле ввода станет кликабельным, затем вводит в поле текст.

        :param by: Стратегия поиска.
        :param locator: Локатор поля ввода.
        :param text: Вводимый текст.
        :param timeout: Время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((by, locator))).send_keys(text)

    @staticmethod
    def get_element_attribute(element: WebElement, attribute_name: str) -> str:
        """
        Возвращает значение атрибута полученного элемента.

        :param element: Полученный элемент.
        :param attribute_name: Имя атрибута.
        """
        return element.get_attribute(attribute_name)

    def get_url(self) -> str:
        """
        Возвращает адрес текущей страницы в браузере.
        """
        return self.driver.current_url

    def mouseover(self, element: WebElement) -> None:
        """
        Наводит курсор на указанный элемент.

        :param element: Указанный элемент.
        """
        ActionChains(self.driver).move_to_element(element).perform()

    def press_enter(self, by: By, locator: str, timeout: int = 10) -> None:
        """
        Ожидает, когда поле ввода станет кликабельным, затем вводит в поле пустое значение.

        :param by: Стратегия поиска.
        :param locator: Локатор поля ввода.
        :param timeout: Время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((by, locator))).send_keys(Keys.ENTER)
