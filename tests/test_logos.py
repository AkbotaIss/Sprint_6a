from pages.main_page import MainPage
from pages.locators.header_locators import HeaderLocators as H

def test_logo_scooter_goes_home(firefox, base_url):
    page = MainPage(firefox, base_url)
    page.open_and_accept()
    page.click(H.LOGO_SCOOTER)
    assert "qa-scooter.praktikum-services.ru" in firefox.current_url

def test_logo_yandex_opens_dzen_new_tab(firefox, base_url):
    page = MainPage(firefox, base_url)
    page.open_and_accept()
    current = firefox.current_window_handle
    page.click(H.LOGO_YANDEX)
    # появится новая вкладка — переключаемся
    for h in firefox.window_handles:
        if h != current:
            firefox.switch_to.window(h)
            break
    assert "dzen.ru" in firefox.current_url
