from selenium.webdriver.common.by import By

class OrderLocators:
    # Шаг 1
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME  = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS    = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO      = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = staticmethod(lambda t: (
        By.XPATH, f"//div[contains(@class,'select-search__select')]//div[normalize-space()='{t}']"
    ))
    PHONE      = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BTN   = (By.XPATH, "//button[.='Далее']")

    # Шаг 2
    DATE       = (By.XPATH, "//input[contains(@placeholder,'Когда привезти самокат')]")
    DATE_CALENDAR_DAY = staticmethod(lambda d: (
        By.XPATH, f"//div[contains(@class,'react-datepicker__day') and not(contains(@class,'outside-month')) and normalize-space()='{d}']"
    ))
    RENT_DROPDOWN = (By.XPATH, "//div[contains(@class,'Dropdown-root')]")
    RENT_TERM    = staticmethod(lambda t: (
        By.XPATH, f"//div[contains(@class,'Dropdown-option') and normalize-space()='{t}']"
    ))
    COLOR_BLACK  = (By.ID, "black")
    COLOR_GREY   = (By.ID, "grey")
    COMMENT      = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BTN    = (By.XPATH, "//button[.='Заказать']")
    CONFIRM_BTN  = (By.XPATH, "//button[normalize-space()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")
