import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


contactname = 'Juliette'
messageTosend='Ceci est un message automatisé : ne pas répondre. Ce Bot est plutôt facile à faire'

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://web.whatsapp.com')

##QR code
print("please scan the QR code")
input()
print("congrats")

###saisir nom du destinataire

input_path_searchContact= '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
input_box_searchContact=driver.find_element(by=By.XPATH, value=input_path_searchContact)
input_box_searchContact.click()
time.sleep(4)

input_box_searchContact.send_keys(contactname)
time.sleep(4)
selected_contact= driver.find_element(by= By.XPATH, value="//span[@Title='"+contactname+"']")
selected_contact.click()
time.sleep(4)


##//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]

input_path_MessageBox = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
input_messageBox = driver.find_element(by=By.XPATH, value=input_path_MessageBox)
time.sleep(4)

#Envoie le message

input_messageBox.send_keys(messageTosend + Keys.ENTER)
time.sleep(15)

##On clôt le script
print('Message Send. Press Enter to quit')
input()
print("Logged out")
driver.quit()


