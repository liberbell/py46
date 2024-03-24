from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
driver.get("https://www.bing.com/")

sleep(1)

search_bar = driver.find_element_by_id("sb_form_q")
search_bar.send_keys("python")

# search_btn = driver.find_element_by_xpath('//path[@class="gray70_fill_sb"]')
# search_btn = driver.find_element_by_xpath('//label/svg')
search_btn = driver.find_element_by_xpath("//label[@for='sb_form_go']")
# search_btn.click()
search_bar.submit()

sleep(2)
for elem in driver.find_elements_by_xpath("//h2[not(contains(@class,'b_topTitleAd'))]/a"):
    print(elem.text)
    print(elem.get_attribute("href"))

next_link = driver.find_element_by_xpath("//a[@title='次のページ']")
driver.get(next_link.get_attribute("href"))
# /html/body/div[2]/div/div[3]/div[2]/form/label/svg/path