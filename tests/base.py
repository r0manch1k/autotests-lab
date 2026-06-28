import pytest
from selenium.webdriver.remote.webdriver import WebDriver


class BaseTest:
    driver: WebDriver

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver
