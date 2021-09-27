import pandas as pd
from selenium import webdriver
driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
whats_app_path = 'https://web.whatsapp.com/'

driver.get(whats_app_path)


data = pd.read_excel(r'contac_list.xlsx', engine='openpyxl')
listdata ="Sagor"





def name_serch():
   #serch_box =driver.find_element_by_class_name('_1Jn3C')
   user_name_div = driver.find_element_by_xpath('//span[@title="{}"]'.format(listdata))
   #user_name_div.send_keys(user_name_div)
   user_name_div.click()


lock = 5

data = int(input("unlock !: "))
if data==lock:
   name_serch()

