from selenium import webdriver
import time
import pandas as pd

option = webdriver.ChromeOptions()

option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe', options=option)
whats_app_path = 'https://web.whatsapp.com/'
driver.get(whats_app_path)

"""xlsx file info"""
data = pd.read_excel(r'contac_list.xlsx', engine='openpyxl')
number_list = list(data['number'])
total_len = len(data)



lock = 5
data = int(input("unlock !: "))
# count = int(input("how manay time you want save : "))

text_content = "boot running successfull"



if data == lock:
   for number in number_list:
      print(number)
      """number search field"""
      element = driver.find_element_by_css_selector("._13NKt ")
      # sending number

      # select user div and click
      user_div = driver.find_element_by_css_selector("._ccCW")

      element.send_keys(number)
      user_div.click()

      send_data_box = driver.find_element_by_class_name('p3_M1')
      time.sleep(2)
      send_data_box.send_keys(text_content)

      time.sleep(2)

      button = driver.find_element_by_class_name('_4sWnG')
      button.click()
      element.clear()
      time.sleep(5)






