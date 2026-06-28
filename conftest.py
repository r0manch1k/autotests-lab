import pytest
from selenium import webdriver
from pages.main import MainPage


@pytest.fixture(scope="function")
def driver():
    options = webdriver.SafariOptions()

    driver = webdriver.Safari(options=options)
    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()


@pytest.fixture
def main(driver):
    return MainPage(driver=driver)
