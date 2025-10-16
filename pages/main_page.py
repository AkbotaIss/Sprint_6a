import allure
from .base_page import BasePage
from .locators.main_locators import MainLocators as L

class MainPage(BasePage):
    @allure.step("Открыть главную и принять cookies")
    def open_and_accept(self):
        self.open("/")
        try:
            self.safe_click(L.ACCEPT_COOKIES)
        except Exception:
            pass

    @allure.step("Развернуть FAQ вопрос #{i} и получить текст ответа")
    def expand_faq_and_get_text(self, i: int) -> str:
        q = self.find(L.FAQ_QUESTION(i))
        self.scroll_into_view(q)
        try:
            q.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", q)
        answer = self.visible(L.FAQ_ANSWER(i))
        return answer.text.strip()

    @allure.step("Клик по кнопке 'Заказать' ({where})")
    def click_order(self, where: str = "top"):
        locator = L.ORDER_TOP if where == "top" else L.ORDER_BOTTOM
        self.safe_click(locator)

