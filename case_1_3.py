from selenium import webdriver
import time
import pandas as pd

option = webdriver.ChromeOptions()

option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe',options=option)
whats_app_path = 'https://web.whatsapp.com/'
driver.get(whats_app_path)

data = pd.read_excel(r'contac_list.xlsx', engine='openpyxl')
data_list = list(data['number'])


lock = 5

data = int(input("unlock !: "))

if data==lock:
   for number in data_list:
      element = driver.find_element_by_css_selector("._13NKt ")
      element.send_keys(number)
      time.sleep(3)
      print(number)
      element.clear()

