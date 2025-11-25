# pages/locators/main_locators.py
from selenium.webdriver.common.by import By


class MainLocators:

    ACCEPT_COOKIES = (By.ID, "rcc-confirm-button")


    ORDER_TOP = (By.XPATH, "(//button[contains(., 'Заказать')])[1]")
    ORDER_BOTTOM = (By.XPATH, "(//button[contains(., 'Заказать')])[last()]")


    ORDER_HEADER = (
        By.XPATH,
        "//*[contains(text(),'Для кого самокат')]"
    )


    @staticmethod
    def FAQ_QUESTION(i: int):
        return By.ID, f"accordion__heading-{i}"

    @staticmethod
    def FAQ_ANSWER(i: int):
        return By.ID, f"accordion__panel-{i}"
