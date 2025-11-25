# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.wait = WebDriverWait(driver, 20)

    def open(self, path: str = ""):
        self.driver.get(self.base_url + path)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_into_view(self, el):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", el
        )

    def click(self, locator):

        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_into_view(el)
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)

    def safe_click(self, locator):

        self.click(locator)

    def open_new_tab_and_switch(self, locator):

        old_tabs = set(self.driver.window_handles)
        self.click(locator)

        # ждём, пока появится новая вкладка
        def new_tab_opened(d):
            return len(set(d.window_handles) - old_tabs) == 1

        self.wait.until(new_tab_opened)

        new_tab = (set(self.driver.window_handles) - old_tabs).pop()
        self.driver.switch_to.window(new_tab)

        # ждём, пока вкладка перестанет быть about:blank
        self.wait.until(lambda d: d.current_url != "about:blank")

    @property
    def current_url(self) -> str:
        return self.driver.current_url
