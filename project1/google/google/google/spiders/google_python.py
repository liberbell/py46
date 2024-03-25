import scrapy
from scrapy_selenium import SeleniumRequest
from time import sleep
from selenium.webdriver.common.keys import keys

class GooglePythonSpider(scrapy.Spider):
    name = "google_python"

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.google.co.jp',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        driver = response.meta["driver"]
        driver.save_screenshot("01_open_google.png")

        search_bar = driver.find_element_by_xpath("//textarea[@name='q']")
        search_bar.send_keys("python")
        sleep(1)

        driver.save_screenshot("02_after_input.png")

        search_bar.send_keys(keys.ENTER)
        sleep(1)

        driver.save_screenshot("03_after_enter.png")
