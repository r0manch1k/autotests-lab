import allure
from pages.main import MainPage
from tests.base import BaseTest


@allure.feature("Тестирование сайта")
class TestMain(BaseTest):
    @allure.story("Главная страница")
    @allure.title("#1: Проверка заголовка главной страницы")
    def test_page_title(self, main: MainPage):
        with allure.step("Открыть главную страницу"):
            main.get("/")
        with allure.step("Проверить, что заголовок содержит название сайта"):
            assert "FreeFEM" in main.title

    @allure.story("Главная страница")
    @allure.title("#2: Отображение панели навигации")
    def test_navbar_visibility(self, main: MainPage):
        main.get("/")
        with allure.step("Проверить видимость главного меню"):
            assert main.find(main.locators.NAVBAR).is_displayed()

    @allure.story("Навигация")
    @allure.title("#3: Переход в раздел загрузок")
    def test_navigate_to_download(self, main: MainPage):
        main.get("/")
        with allure.step("Кликнуть по разделу загрузок в меню"):
            main.click_download_menu()
        with allure.step("Проверить заголовок страницы загрузок"):
            assert "download" in main.get_main_header_text().lower()

    @allure.story("Раздел загрузок")
    @allure.title("#4: Наличие ссылки на репозиторий")
    def test_github_link_exists(self, main: MainPage):
        main.get("/download/")
        with allure.step("Проверить присутствие ссылки на репозиторий"):
            assert main.find(main.locators.GITHUB_LINK).is_displayed()

    @allure.story("Навигация")
    @allure.title("#5: Переход в раздел документации")
    def test_navigate_to_documentation(self, main: MainPage):
        main.get("/")
        with allure.step("Кликнуть по разделу документации в меню"):
            main.click_documentation_menu()
        with allure.step("Проверить заголовок страницы документации"):
            assert "documentation" in main.get_main_header_text().lower()

    @allure.story("Страница документации")
    @allure.title("#6: Наличие ссылки на руководства")
    def test_manual_link_exists(self, main: MainPage):
        main.get("/documentation/")
        with allure.step("Проверить наличие основного блока документации"):
            assert main.find(main.locators.MANUAL_LINK).is_displayed()

    @allure.story("Навигация")
    @allure.title("#7: Переход в раздел галереи примеров")
    def test_navigate_to_gallery(self, main: MainPage):
        main.get("/")
        with allure.step("Кликнуть по разделу галереи в меню"):
            main.click_gallery_menu()
        with allure.step("Проверить заголовок страницы галереи"):
            assert "gallery" in main.get_main_header_text().lower()

    @allure.story("Навигация")
    @allure.title("#8: Переход в раздел возможностей")
    def test_navigate_to_features(self, main: MainPage):
        main.get("/")
        with allure.step("Кликнуть по разделу возможностей в меню"):
            main.click_features_menu()
        with allure.step("Проверить заголовок страницы возможностей"):
            assert "features" in main.get_main_header_text().lower()

    @allure.story("Навигация")
    @allure.title("#9: Переход в раздел сообщества")
    def test_navigate_to_community(self, main: MainPage):
        main.get("/")
        with allure.step("Кликнуть по разделу сообщества в меню"):
            main.click_community_menu()
        with allure.step("Проверить заголовок страницы сообщества"):
            assert "community" in main.get_main_header_text().lower()

    @allure.story("Главная страница")
    @allure.title("#10: Отображение футера страницы")
    def test_footer_visibility(self, main: MainPage):
        main.get("/")
        with allure.step("Проверить видимость футера сайта"):
            assert main.find(main.locators.FOOTER).is_displayed()
