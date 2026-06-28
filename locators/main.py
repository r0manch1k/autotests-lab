from selenium.webdriver.common.by import By


class MainPageLocators:
    NAVBAR = (By.CSS_SELECTOR, "nav.navbar")
    FOOTER = (By.CSS_SELECTOR, "footer")
    HEADER = (By.CSS_SELECTOR, "h1")

    LINK_DOWNLOAD = (By.XPATH, "//a[contains(@href, 'download')]")
    LINK_DOCUMENTATION = (By.XPATH, "//a[contains(@href, 'documentation')]")
    LINK_GALLERY = (By.XPATH, "//a[contains(@href, 'gallery')]")
    LINK_FEATURES = (By.XPATH, "//a[contains(@href, 'features')]")
    LINK_COMMUNITY = (By.XPATH, "//a[contains(@href, 'community')]")

    LINK_GITHUB = (By.XPATH, "//a[contains(@href, 'github.com/FreeFem')]")
    LINK_MANUAL = (By.CSS_SELECTOR, "a[href*='documentation']")
