### requirments : pyautogui, webbrowser

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pyautogui

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://web.whatsapp.com')

##QR code
print("please scan the QR code")
input()
print("congrats")


#SPAM
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('HI')
    pyautogui.press('enter')