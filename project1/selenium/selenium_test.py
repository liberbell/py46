from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://www.bing.com/")

search_bar = driver.find_element_by_id("sb_form_q")
search_bar.send_keys("python")

# search_btn = driver.find_element_by_xpath('//path[@class="gray70_fill_sb"]')
# search_btn = driver.find_element_by_xpath('//label/svg')
search_btn = driver.find_element_by_xpath("//label[@for='sb_form_go']")
# search_btn.click()
search_bar.submit()

sleep(2)
driver.find_elements_by_xpath("//div[@class='b_title']/h2/a")
# /html/body/div[2]/div/div[3]/div[2]/form/label/svg/path