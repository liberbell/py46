from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://www.bing.com/")

search_bar = driver.find_element_by_id("sb_form_q")
search_bar.send_keys("python")

search_btn = driver.find_element_by_xpath('//label[@for="sb_form_go"]')
search_btn.click()