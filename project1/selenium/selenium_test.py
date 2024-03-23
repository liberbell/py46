from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://www.bing.com/")