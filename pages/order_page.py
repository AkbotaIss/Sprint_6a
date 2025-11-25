# pages/order_page.py

import allure
from datetime import datetime, timedelta

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from .locators.order_locators import OrderLocators as L


class OrderPage(BasePage):

    @allure.step("Шаг 1: {first} {last}, адрес: {address}, метро: {metro}, телефон: {phone}")
    def fill_step1(self, first, last, address, metro, phone):

        first_el = self.find(L.FIRST_NAME)
        first_el.clear()
        first_el.send_keys(first)


        last_el = self.find(L.LAST_NAME)
        last_el.clear()
        last_el.send_keys(last)


        addr_el = self.find(L.ADDRESS)
        addr_el.clear()
        addr_el.send_keys(address)


        metro_input = self.find(L.METRO)
        self.scroll_into_view(metro_input)
        metro_input.clear()
        metro_input.send_keys(metro)
        try:
            self.safe_click(L.METRO_OPTION(metro))
        except Exception:
            metro_input.send_keys(Keys.ARROW_DOWN)
            metro_input.send_keys(Keys.ENTER)


        phone_el = self.find(L.PHONE)
        phone_el.clear()
        phone_el.send_keys(phone)


        self.safe_click(L.NEXT_BTN)

    @allure.step("Шаг 2: дата, срок '{term}', цвет {color}, коммент '{comment}'")
    def fill_step2(self, day: int, term: str, color: str, comment: str):


        self.visible(L.STEP2_HEADER)


        date_input = self.visible(L.DATE)
        self.scroll_into_view(date_input)


        today = datetime.today()
        try:
            candidate = today.replace(day=int(day))
            if candidate <= today:
                candidate = today + timedelta(days=1)
        except Exception:
            candidate = today + timedelta(days=1)

        target = candidate.strftime("%d.%m.%Y")


        date_input.click()
        try:
            date_input.send_keys(Keys.COMMAND, "a")  # macOS
        except Exception:
            date_input.send_keys(Keys.CONTROL, "a")  # windows/linux
        date_input.send_keys(target)
        date_input.send_keys(Keys.ENTER)


        self.safe_click(L.RENT_DROPDOWN)
        self.safe_click(L.RENT_TERM(term))


        if color.lower().startswith("ч"):
            self.safe_click(L.COLOR_BLACK)
        else:
            self.safe_click(L.COLOR_GREY)


        if comment:
            comment_el = self.find(L.COMMENT)
            comment_el.clear()
            comment_el.send_keys(comment)


        self.safe_click(L.ORDER_BTN)

    @allure.step("Подтвердить заказ")
    def confirm(self):
        self.safe_click(L.CONFIRM_BTN)

    def success_modal_visible(self):
        try:
            return self.visible(L.SUCCESS_MODAL)
        except TimeoutException:
            return None

    @allure.step("Проверяем, что открылась форма заказа (шаг 1)")
    def is_order_form_open(self) -> bool:
        try:
            header = self.visible(L.ORDER_HEADER)
            return header.is_displayed()
        except TimeoutException:
            return False
