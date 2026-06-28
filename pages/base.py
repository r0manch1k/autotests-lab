from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


class BasePage:
    driver: WebDriver

    base_url: str

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def get(self, path: str = "") -> None:
        self.driver.get(self.base_url + path)

    def find(self, locator, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: tuple, timeout=10) -> None:
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    @property
    def url(self) -> str:
        return self.driver.current_url

    @property
    def title(self) -> str:
        return self.driver.title
