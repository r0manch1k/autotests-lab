import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main import MainPage


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")

    manager = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=Service(manager), options=options)

    yield driver
    driver.quit()


@pytest.fixture
def main(driver):
    return MainPage(driver=driver)
