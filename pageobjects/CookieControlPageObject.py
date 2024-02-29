import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.connection import Connection


class CookiesControl:

    def __init__(self, connection: Connection):
        self.conn = connection

    def accept_cookies(self):
        # accept cookies
        cookie_dialog = self.conn.driver.find_element(By.ID, "CybotCookiebotDialog")
        elem = self.conn.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        elem.click()
        WebDriverWait(self.conn.driver, 10).until(EC.any_of(EC.staleness_of(cookie_dialog), EC.invisibility_of_element(cookie_dialog)))
        time.sleep(2)

