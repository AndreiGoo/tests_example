import pytest

from selenium.webdriver.common.by import By
from selenium import webdriver

from appium import webdriver as appium_webdriver

from pages.web.categories import Categories
from pages.web.items_list import ItemsList
from pages.web.order_status import OrderStatus
from pages.web.main_page import MainPage

from pages.mobile.premium_subscription_window import PremiumSubscriptionWindow
from pages.mobile.conversions import Conversions

from data.web.categories import (Appliances,
                                 EmbeddedTechnology,
                                 Hobs,
                                 ElectricHobs)
from data.web.orders import OrdersText
from data.web.main_page import MainPageText
from data.web.test_data import Routes

from data.mobile.configuration_data import (CAPABILITIES,
                                            BASE_HOST)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Routes.main_page)
    yield driver
    driver.quit()


@pytest.fixture
def items_list(driver):
    categories = Categories(driver)
    categories.click_link_by_text(Appliances.appliances)
    categories.choose_categories(EmbeddedTechnology.embedded_technology,
                                 Hobs.hobs,
                                 ElectricHobs.electric_hobs)
    return ItemsList(driver)


@pytest.fixture
def order_status(driver):
    main_pages = MainPage(driver)
    main_pages.click_link_by_text(MainPageText.buyers,
                                  MainPageText.status)
    return OrderStatus(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def mobile_driver():
    driver = appium_webdriver.Remote(command_executor=BASE_HOST,
                                     desired_capabilities=CAPABILITIES)
    yield driver
    driver.quit()


@pytest.fixture
def close_popup(mobile_driver):
    window = PremiumSubscriptionWindow(mobile_driver)
    window.close_popup()
    return mobile_driver


@pytest.fixture
def conversions(close_popup):
    return Conversions(close_popup)
