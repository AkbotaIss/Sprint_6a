import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urls import BASE_URL


@pytest.fixture
def firefox():

    options = Options()
    options.add_argument("--width=1280")
    options.add_argument("--height=1024")

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def base_url():

    return BASE_URL
