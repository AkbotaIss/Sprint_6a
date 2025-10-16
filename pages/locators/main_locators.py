from selenium.webdriver.common.by import By
class MainLocators:
    ACCEPT_COOKIES = (By.ID, "rcc-confirm-button")
    ORDER_TOP = (By.XPATH, "//button[contains(., 'Заказать')][1]")
    ORDER_BOTTOM = (By.XPATH, "(//button[contains(., 'Заказать')])[last()]")
    FAQ_QUESTION = staticmethod(lambda i: (By.ID, f"accordion__heading-{i}"))
    FAQ_ANSWER   = staticmethod(lambda i: (By.ID, f"accordion__panel-{i}"))
