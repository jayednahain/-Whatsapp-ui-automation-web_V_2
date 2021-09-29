from selenium import webdriver
import time
import pandas as pd


driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
whats_app_path = 'https://web.whatsapp.com/'
driver.get(whats_app_path)

data = pd.read_excel(r'contac_list.xlsx', engine='openpyxl')
data_list = list(data['number'])


lock = 5
data = int(input("unlock !: "))

if data==lock:
   for i in range(len(data)):
      element = driver.find_element_by_css_selector("._13NKt ")
      element.send_keys(data_list[i])
      time.sleep(3)
      element.clear()

