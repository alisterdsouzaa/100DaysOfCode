from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # To avoid closing of Chrome Browser

driver = webdriver.Chrome(chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# total_num_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(total_num_of_articles.text)
# total_num_of_articles.click()

all_ports = driver.find_element(By.LINK_TEXT, "Storm Daniel")
# all_ports.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
