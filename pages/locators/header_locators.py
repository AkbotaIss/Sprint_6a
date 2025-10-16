from selenium.webdriver.common.by import By

class HeaderLocators:
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'ScooterLogo')]")
    LOGO_YANDEX  = (By.XPATH, "//a[contains(@class,'YandexLogo')]")
