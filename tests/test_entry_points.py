# tests/test_entry_points.py
import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Order entry points")
class TestEntryPoints:
    @allure.title("Кнопка «Заказать» ({where}) открывает форму заказа")
    @pytest.mark.ui
    @pytest.mark.parametrize("where", ["top", "bottom"])
    def test_entry_points_open_order_form(self, firefox, base_url, where):
        """
        Проверяем, что обе кнопки «Заказать» (верхняя и нижняя)
        действительно открывают форму оформления заказа.
        """
        main = MainPage(firefox, base_url)
        order = OrderPage(firefox, base_url)

        # Открыть главную и принять cookies
        main.open_and_accept()

        # Нажать на нужную кнопку «Заказать»
        main.click_order(where=where)

        # Проверить, что форма заказа (шаг 1) открылась
        assert order.is_order_form_open(), "Форма заказа не открылась"
