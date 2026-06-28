from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


class BasePage:
    driver: WebDriver

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def get(self, base: str, path: str = "") -> None:
        self.driver.get(base + path)

    def find(self, locator, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: tuple, timeout=10) -> None:
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @property
    def url(self) -> str:
        return self.driver.current_url

    @property
    def title(self) -> str:
        return self.driver.title
