import selenium.webdriver


class Connection:
    def __init__(self, driver: selenium.webdriver):
        self.driver = driver
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(10)

    def load_url(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def refresh(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
