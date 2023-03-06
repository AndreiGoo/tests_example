import allure

from data.mobile.conversions_categories import ConversionsText
from data.mobile.temperature_units import TemperatureUnits
from data.mobile.test_data_mobile import Values


@allure.title("Преобразование значений температуры")
@allure.severity("Normal")
def test_temperature_conversion(conversions):
    conversions.choose_category(ConversionsText.temperature)
    conversions.choose_unit_from(TemperatureUnits.celsius)
    conversions.choose_unit_to(TemperatureUnits.fahrenheit)
    assert conversions.check_celsius_to_fahrenheit_conversion(Values.temperature_values), \
        "Преобразование выполнено неверно."
