# pages/locators/order_locators.py
from selenium.webdriver.common.by import By


class OrderLocators:


    # ---------------------- Заголовок формы ----------------------
    ORDER_HEADER = (
        By.XPATH,
        "//*[contains(text(),'Для кого самокат')]"
    )


    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")

    @staticmethod
    def METRO_OPTION(text: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'select-search__select')]//div[normalize-space()='{text}']"
        )

    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BTN = (By.XPATH, "//button[.='Далее']")



    STEP2_HEADER = (
        By.XPATH,
        "//div[contains(text(), 'Про аренду')]"
    )

    DATE = (By.XPATH, "//input[contains(@placeholder,'Когда привезти самокат')]")

    @staticmethod
    def DATE_CALENDAR_DAY(day: str):
        return (
            By.XPATH,
            "//div[contains(@class,'react-datepicker__day') and not(contains(@class,'outside-month')) "
            f"and normalize-space()='{day}']"
        )

    RENT_DROPDOWN = (By.XPATH, "//div[contains(@class,'Dropdown-root')]")

    @staticmethod
    def RENT_TERM(term: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'Dropdown-option') and normalize-space()='{term}']"
        )

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BTN = (By.XPATH, "//button[.='Заказать']")
    CONFIRM_BTN = (By.XPATH, "//button[normalize-space()='Да']")

    SUCCESS_MODAL = (
        By.XPATH,
        "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]"
    )
