import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

BASE_URL = "https://qa-scooter.praktikum-services.ru"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def firefox():
    options = Options()
    driver = webdriver.Firefox(options=options)  # Selenium Manager скачает драйвер
    driver.set_window_size(1366, 900)
    yield driver
    driver.quit()
