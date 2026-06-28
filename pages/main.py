from pages.base import BasePage
from locators.main import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_download_menu(self):
        self.click_elem(self.locators.LINK_DOWNLOAD)

    def click_documentation_menu(self):
        self.click_elem(self.locators.LINK_DOCUMENTATION)

    def click_gallery_menu(self):
        self.click_elem(self.locators.LINK_GALLERY)

    def click_features_menu(self):
        self.click_elem(self.locators.LINK_FEATURES)

    def click_community_menu(self):
        self.click_elem(self.locators.LINK_COMMUNITY)

    def get_main_header_text(self):
        return self.find_elem(self.locators.HEADER).text
