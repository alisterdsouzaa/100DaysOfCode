from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
total_num_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(total_num_of_articles.text)
