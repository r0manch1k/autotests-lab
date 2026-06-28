from pages.base import BasePage
from locators.main import MainPageLocators


class MainPage(BasePage):
    base_url = "https://freefem.org"

    locators = MainPageLocators()

    def click_download_menu(self):
        self.click(self.locators.LINK_DOWNLOAD)

    def click_documentation_menu(self):
        self.click(self.locators.LINK_DOCUMENTATION)

    def click_gallery_menu(self):
        self.click(self.locators.LINK_GALLERY)

    def click_features_menu(self):
        self.click(self.locators.LINK_FEATURES)

    def click_community_menu(self):
        self.click(self.locators.LINK_COMMUNITY)

    def get_main_header_text(self):
        return self.find(self.locators.HEADER).text
