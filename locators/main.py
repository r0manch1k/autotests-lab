from selenium.webdriver.common.by import By


class MainPageLocators:
    NAVBAR = (By.CSS_SELECTOR, "nav#nav")
    FOOTER = (By.CSS_SELECTOR, "footer")
    HEADER = (By.CSS_SELECTOR, "h1")

    LINK_DOWNLOAD = (By.CSS_SELECTOR, "#download a")
    LINK_DOCUMENTATION = (By.CSS_SELECTOR, "nav#nav a[href*='doc']")
    LINK_GALLERY = (By.CSS_SELECTOR, "nav#nav a[href*='gallery']")
    LINK_FEATURES = (
        By.CSS_SELECTOR,
        "nav#nav a[href*='modules']",
    )
    LINK_COMMUNITY = (By.CSS_SELECTOR, "nav#nav a[href*='community']")

    LINK_GITHUB = (By.CSS_SELECTOR, "nav#nav a[href*='github.com']")
    LINK_MANUAL = (By.CSS_SELECTOR, "a[href*='doc']")
