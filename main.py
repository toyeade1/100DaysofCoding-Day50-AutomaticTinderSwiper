from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import time

opt = Options()
opt.add_experimental_option('detach', True)
path = '/Users/a/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver'
ser = Service(path)
driver = webdriver.Chrome(service=ser, options=opt)

# Loading up tinder

driver.get('https://tinder.com/')
time.sleep(2)
# Logging into tinder account
# login button:
driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(1)
main_handle = driver.current_window_handle
print(main_handle)
# Continue with Google button:
driver.find_element('xpath', '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[1]/div/button').click()
# driver.find_element('xpath', '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[1]/div/div/div/iframe').click()
time.sleep(2)
all_handles = driver.window_handles
pop_up = all_handles[1]

# Switch to login window
driver.switch_to.window(pop_up)
time.sleep(2)

# Find the Email sign in field
email = driver.find_element('xpath', '//*[@id="identifierId"]')
email.send_keys(os.environ['username'])

# Clicking Next
next_button = driver.find_element('xpath', '//*[@id="identifierNext"]/div/button')
next_button.click()
time.sleep(2)

# Enter Password
password = driver.find_element('xpath', '//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(os.environ['password'])
time.sleep(2)

# Click Next Again
driver.find_element('xpath', '//*[@id="passwordNext"]/div/button').click()
time.sleep(2)

# Switch Back to the main window
driver.switch_to.window(main_handle)
time.sleep(2)

# Allow Using my Location:
driver.find_element('xpath', '//*[@id="s1903812341"]/main/div/div/div/div[3]/button[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="s1903812341"]/main/div/div/div/div[3]/button[2]').click()
time.sleep(6)
driver.find_element('xpath', '//*[@id="s1903812341"]/main/div/div[2]/button').click()
time.sleep(3)

# Start Swiping:
swiping = True
driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div['
                                 '4]/div/div[4]/button').click()
time.sleep(2)

while swiping:
    driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div['
                                 '5]/div/div[4]/button').click()
    time.sleep(2)
