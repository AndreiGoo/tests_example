from dataclasses import dataclass


@dataclass
class Routes:
    """Класс, хранящий адреса страниц."""

    main_page: str = "https://www.dns-shop.ru/"
    cart: str = "cart/"

    base_api = "https://restapi.dns-shop.ru/v1"
    get_presearch = "/get-presearch"
