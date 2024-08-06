from selenium import webdriver


class WebDriverManager:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_url(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()