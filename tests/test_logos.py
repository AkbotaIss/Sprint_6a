# tests/test_logos.py
import allure

from pages.main_page import MainPage
from urls import BASE_URL


@allure.feature("Navigation")
class TestLogos:

    @allure.story("Клик по логотипу Самоката ведёт на главную страницу")
    @allure.title("Переход по логотипу Самоката на главную")
    def test_logo_scooter_goes_home(self, firefox, base_url):
        page = MainPage(firefox, base_url)
        page.open_and_accept()

        page.click_logo_scooter()

        assert page.current_url.startswith(BASE_URL)

    @allure.story("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    @allure.title("Переход по логотипу Яндекс в Дзен/Яндекс")
    def test_logo_yandex_opens_dzen_new_tab(self, firefox, base_url):
        page = MainPage(firefox, base_url)
        page.open_and_accept()

        page.open_dzen_in_new_tab()


        url = page.current_url
        assert (
            "dzen.ru" in url
            or "passport.yandex.ru" in url
            or "showcaptcha" in url
        ), f"Неожиданный URL после клика по логотипу Яндекса: {url}"
