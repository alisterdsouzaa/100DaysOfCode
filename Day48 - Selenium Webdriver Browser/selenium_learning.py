from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver"

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds

driver.get("https://www.python.org/")
event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}
for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.close()
