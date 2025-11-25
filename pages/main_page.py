# pages/main_page.py
import allure
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from .locators.main_locators import MainLocators as L
from .locators.header_locators import HeaderLocators as H


class MainPage(BasePage):

    @allure.step("Открыть главную страницу и принять cookies")
    def open_and_accept(self):
        self.open("/")
        try:

            self.click(L.ACCEPT_COOKIES)
        except TimeoutException:

            pass

    @allure.step("Развернуть FAQ-вопрос №{i} и получить текст ответа")
    def expand_faq_and_get_text(self, i: int) -> str:

        self.click(L.FAQ_QUESTION(i))


        answer = self.visible(L.FAQ_ANSWER(i))
        return answer.text.strip()

    @allure.step("Клик по кнопке 'Заказать' ({where})")
    def click_order(self, where: str = "top"):
        """
        where: 'top' или 'bottom'
        """
        locator = L.ORDER_TOP if where == "top" else L.ORDER_BOTTOM
        self.click(locator)

    @allure.step("Клик по логотипу Самоката")
    def click_logo_scooter(self):
        self.click(H.LOGO_SCOOTER)

    @allure.step("Открыть Яндекс.Дзен в новой вкладке")
    def open_dzen_in_new_tab(self):
        self.open_new_tab_and_switch(H.LOGO_YANDEX)
