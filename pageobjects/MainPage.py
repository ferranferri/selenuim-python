import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.CookieControlPageObject import CookiesControl
from utils.connection import Connection


class AbstractMainPage:
    def __init__(self):
        pass

    def load(self, connection: Connection):
        cookie_control = CookiesControl(connection)
        cookie_control.accept_cookies()

    def get_main_title(self, connection: Connection):
        title = connection.driver.find_element(By.CSS_SELECTOR,
                                               "body > section.hero-simple.l-hero-simple.bg-color-white.u-dots-bg > div > div > div > div > h1")
        return title.text
        pass


class EnglishMainPage(AbstractMainPage):
    def load(self, connection: Connection):
        connection.driver.get("https://www.datacolor.com/")
        AbstractMainPage.load(self, connection)


class SpanishMainPage(AbstractMainPage):
    def load(self, connection: Connection):
        connection.driver.get("https://www.datacolor.com/es/")
        AbstractMainPage.load(self, connection)


class MainPageFactory:
    @classmethod
    def create_main_page(self, language: str):
        if language == "English":
            return EnglishMainPage()
        if language == "Spanish":
            return SpanishMainPage()
