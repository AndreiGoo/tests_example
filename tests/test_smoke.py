import allure

from data.web.orders import OrdersText
from data.web.login_window import LoginWindow


@allure.title("Добавление товара в корзину")
@allure.severity("Normal")
def test_add_in_cart(items_list):
    item_code_list = items_list.get_first_item_code_list()
    items_list.buy_first_item()
    assert items_list.check_modal_window_displayed(), "Модальное окно не появилось."
    assert items_list.check_button_text_changes(), "Текст на кнопке не изменился."

    items_list.open_cart()
    assert items_list.check_url_cart(), "Неверный адрес корзины."

    item_code_cart = items_list.get_first_item_code_cart()
    assert item_code_list == item_code_cart, "Товар в списке не совпадает с товаром в корзине."


@allure.title("Получение статуса заказа")
@allure.severity("Normal")
def test_order_status(order_status):
    order_status.send_keys_by_text(OrdersText.phone,
                                   OrdersText.invalid_phone_value)
    order_status.send_keys_by_text(OrdersText.order_number,
                                   OrdersText.invalid_order_number_value)

    order_status.show_order_status()
    assert order_status.check_error_message(OrdersText.error_message_phone),\
           'Сообщение "Телефон указан неверно" не появилось.'
    assert order_status.check_error_message(OrdersText.error_message_number),\
           'Сообщение "Номер заказа указан неверно" не появилось.'


@allure.title("Некорректный вход")
@allure.severity("Normal")
def test_invalid_login(main_page):
    main_page.mouseover_login_menu()

    main_page.press_login_button()

    main_page.send_empty_field()
    assert main_page.check_error_message(LoginWindow.error_message), 'Сообщение "Заполните поле" не появилось.'
