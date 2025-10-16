import time
import allure
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from .locators.order_locators import OrderLocators as L


class OrderPage(BasePage):

    @allure.step("Шаг 1: {first} {last}, адрес: {address}, метро: {metro}, телефон: {phone}")
    def fill_step1(self, first, last, address, metro, phone):
        self.find(L.FIRST_NAME).clear(); self.find(L.FIRST_NAME).send_keys(first)
        self.find(L.LAST_NAME).clear();  self.find(L.LAST_NAME).send_keys(last)
        self.find(L.ADDRESS).clear();    self.find(L.ADDRESS).send_keys(address)

        metro_input = self.find(L.METRO)
        self.scroll_into_view(metro_input)
        metro_input.clear(); metro_input.send_keys(metro)
        # пробуем выбрать из списка, если нет — Enter
        try:
            self.safe_click(L.METRO_OPTION(metro))
        except Exception:
            metro_input.send_keys(Keys.ARROW_DOWN); metro_input.send_keys(Keys.ENTER)

        self.find(L.PHONE).clear(); self.find(L.PHONE).send_keys(phone)
        self.safe_click(L.NEXT_BTN)
        time.sleep(0.5)

    @allure.step("Шаг 2: дата, срок '{term}', цвет {color}, коммент '{comment}'")
    def fill_step2(self, day: int, term: str, color: str, comment: str) -> None:
        # ждём перехода на шаг 2 — появление поля даты
        date_input = self.wait.until(EC.visibility_of_element_located(L.DATE))
        self.scroll_into_view(date_input)

        # формируем «безопасную» дату:
        # если day из набора уже прошёл или невалиден — берём завтра
        today = datetime.today()
        try:
            candidate = today.replace(day=int(day))
            if candidate <= today:
                candidate = today + timedelta(days=1)
        except Exception:
            candidate = today + timedelta(days=1)
        target = candidate.strftime("%d.%m.%Y")

        # вводим дату напрямую (без календаря)
        date_input.click()
        try:
            date_input.send_keys(Keys.COMMAND, "a")   # macOS
        except Exception:
            date_input.send_keys(Keys.CONTROL, "a")   # win/linux
        date_input.send_keys(target)
        date_input.send_keys(Keys.ENTER)

        # срок аренды
        self.safe_click(L.RENT_DROPDOWN)
        self.safe_click(L.RENT_TERM(term))

        # цвет
        if color.lower().startswith("ч"):
            self.safe_click(L.COLOR_BLACK)
        else:
            self.safe_click(L.COLOR_GREY)

        # комментарий (если есть)
        if comment:
            self.find(L.COMMENT).clear()
            self.find(L.COMMENT).send_keys(comment)

        # оформить заказ
        self.safe_click(L.ORDER_BTN)

    @allure.step("Подтвердить заказ")
    def confirm(self):
        self.safe_click(L.CONFIRM_BTN)

    def success_modal_visible(self):
        try:
            return self.visible(L.SUCCESS_MODAL)
        except TimeoutException:
            return None
