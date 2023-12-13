# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Encode Message Text
with open('message.txt', 'r') as file:
    msg = file.read()

numbers = []
with open('numbers.txt', 'r') as file:
    for num in file.readlines():
        numbers.append(num.rstrip())

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(10)

for num in numbers :
    link2 = f'https://web.whatsapp.com/send?phone={num}&text={msg}'
    driver.get(link2)
    time.sleep(10)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(10)
time.sleep(20)

