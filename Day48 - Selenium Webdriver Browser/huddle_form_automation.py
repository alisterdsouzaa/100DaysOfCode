import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Get today's date
# Format the date as "dd-mm-yyyy"
todays_date = datetime.now().strftime("%d-%m-%Y")

with open(r"C:\Users\Alister\Desktop\Huddle_Form_Automation\my_updates.txt", 'r') as file:
    MY_TASKS = file.readlines()

EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
MY_EMAIL = os.environ.get("MY_EMAIL")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # To avoid closing of Chrome Browser

driver = webdriver.Chrome(chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc8jsaZlEM0GvKoFtrKGuQXj3Y-V0h7OKDophgpnpQJgz5jQQ/viewform")

email = driver.find_element(By.NAME, "identifier")
email.send_keys(MY_EMAIL)
print("Email entered successfully...")

click_next = driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div["
                                 "1]/div/div/button")
click_next.click()
print("Clicked successfully...")
time.sleep(5)

password = driver.find_element(By.NAME, "Passwd")
password.send_keys(EMAIL_PASSWORD)
print("Password entered successfully...")

click_next_password = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div["
                                                    "2]/div/div[1]/div/div/button/span")
click_next_password.click()
print("Clicked successfully...")

time.sleep(5)

clear_form = driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[2]/div[2]/div/span/span")
clear_form.click()
time.sleep(2)
# clear_form_1 = driver.find_element(By.XPATH, "//span[contains(text(), 'Clear form')]")
clear_form_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span")
# "/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span"
clear_form_1.click()

time.sleep(0.5)

email_check_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div['
                                                '1]/label/div/div[1]/div[2]')
print("Email check box ...")
email_check_box.click()
print("email checkbox clicked successfully...")

time.sleep(0.5)

session_selection_to_FW = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div['
                                                        '2]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
print("Firmware team session check box reached")
session_selection_to_FW.click()
print("Firmware team session check box clicked...")

print("Project selection reached")
project_selection = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div["
                                                  "2]/div/div/span/div/div[12]/label/div/div[1]/div/div[3]/div")
project_selection.click()
print("Project selection complete")

firmware_team_selection = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["
                                                        "4]/div/div/div[2]/div/div/span/div/div[3]/label/div/div["
                                                        "2]/div/span")
print("firmware team selection reached")
firmware_team_selection.click()
print("firmware team selection complete")

details_of_work_done = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["
                                                     "6]/div/div/div[2]/div/div[1]/div[2]/textarea")
details_of_work_done.send_keys(MY_TASKS)

status = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div["
                                       "1]/div[1]/div[1]")
status.click()
time.sleep(0.5)
status_initiated = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div["
                                                 "2]/div/div[2]/div[4]/span")
status_initiated.click()
time.sleep(0.5)
copy_of_responses = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/label/div")
time.sleep(0.5)
copy_of_responses.click()
time.sleep(0.5)
print("Date...")

date = driver.find_element(By.XPATH, "//input[@type='date']")
# date.click()
date.send_keys(todays_date)
print("Date clicked")
# date.send_keys(Keys.ENTER)
print("Date entered")

# submit_form = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[2]/div[1]"
#                                             "/div/span/span")
# submit_form.click()
