import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage

ORDER_HEADER = (By.XPATH, "//*[contains(text(),'Для кого самокат')]")

@pytest.mark.ui
@pytest.mark.parametrize("where", ["top", "bottom"])
def test_entry_points_open_order_form(firefox, base_url, where):
    main = MainPage(firefox, base_url)
    main.open_and_accept()
    main.click_order(where)
    assert main.visible(ORDER_HEADER)
