from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 12)

    def open(self, path=""):
        self.driver.get(self.base_url + path)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_into_view(self, el):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)

    def safe_click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_into_view(el)
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)
