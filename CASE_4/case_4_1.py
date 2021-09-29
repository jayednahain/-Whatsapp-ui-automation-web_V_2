from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
whats_app_path = 'https://web.whatsapp.com/'
driver.get(whats_app_path)

"""load data"""
data = pd.read_excel(r'contac_list.xlsx', engine='openpyxl')
#clean NUll
new_data = data.fillna("No value")
number_list = list(new_data['number'])



lock = 5
data = int(input("unlock !: "))

if lock == data:
   for i in range(len(new_data)):

      """find user"""
      element = driver.find_element_by_css_selector("._13NKt ")
      element.send_keys(number_list[i])
      time.sleep(3)
      user_div = driver.find_element_by_css_selector("._ccCW")
      user_div.click()
      time.sleep(3)


      """sendig data"""
      send_data_box = driver.find_element_by_class_name('p3_M1')
      time.sleep(1)
      checK_xpath_read = driver.find_elements_by_xpath('//span[@aria-label=" Read "]')
      time.sleep(1)
      try:
         checK_xpath_unread = driver.find_elements_by_xpath('//span[@aria-label=" Delivered "]')
      except NoSuchElementException as se:
         print("no unread text")
         pass
      time.sleep(2)

      if len(checK_xpath_unread)==0:
         new_data.at[i, 'status'] = 'seen'
         print("push seen")
      elif len(checK_xpath_unread)>0:
         new_data.at[i, 'status'] = 'unseen'
         print("push unseen")


      print("total read tex", len(checK_xpath_read))
      print("total underad tex", len(checK_xpath_unread))
      time.sleep(1)
      print("--------------")
      element.clear()

time.sleep(3)
new_data.to_excel('out_put/status_check_.xlsx')
print(new_data)





