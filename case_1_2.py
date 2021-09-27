from selenium import webdriver
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException


option = webdriver.ChromeOptions()

option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe',options=option)
whats_app_path = 'https://web.whatsapp.com/'

driver.get(whats_app_path)
#time.sleep(15)



data = pd.read_excel(r'contac_list.xlsx', engine='openpyxl')
#data_list = list(data['name'])
data_list= ['Niloy']


for name in data_list:
   try:
      user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
      user.click()
      print("found !")
   except NoSuchElementException as se:
      pass
