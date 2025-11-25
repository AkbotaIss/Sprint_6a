# pages/locators/header_locators.py
from selenium.webdriver.common.by import By


class HeaderLocators:
    """Локаторы элементов в шапке сайта (хедере)."""


    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")


    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
