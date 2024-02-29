import pytest
from selenium import webdriver
from pageobjects.MainPage import MainPageFactory
from utils.connection import Connection


class TestMainPage:
    connection: Connection

    @classmethod
    def setup_class(cls):
        TestMainPage.connection = Connection(webdriver.Chrome())

    @classmethod
    def teardown_class(cls):
        TestMainPage.connection.close()

    @pytest.mark.parametrize('lang,expected_title', [
        ('English', "Cost-Effective + Smart Color Solutions that Perfectly Fit Your Workflows"),
        ('Spanish', "Soluciones de color rentables e inteligentes que se adaptan perfectamente a sus flujos de trabajo"),
    ])
    def test_title_on_language(self, lang, expected_title):
        TestMainPage.connection.refresh()
        main_page = MainPageFactory.create_main_page(lang)
        main_page.load(TestMainPage.connection)
        title = main_page.get_main_title(TestMainPage.connection)
        assert title == expected_title
