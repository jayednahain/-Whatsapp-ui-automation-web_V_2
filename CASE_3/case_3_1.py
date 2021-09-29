from selenium import webdriver
import time
import pandas as pd



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


text_content = "test massage"

if lock == data:
   for i in range(len(new_data)):

      """find user"""
      element = driver.find_element_by_css_selector("._13NKt ")
      element.send_keys(number_list[i])
      time.sleep(5)
      user_div = driver.find_element_by_css_selector("._ccCW")
      user_div.click()
      time.sleep(4)

      """send data"""
      send_data_box = driver.find_element_by_class_name('p3_M1')
      send_data_box.send_keys(text_content)
      time.sleep(2)
      """send button"""
      button = driver.find_element_by_class_name('_4sWnG')
      button.click()

      """push data to xl file"""
      new_data.at[i,'delivery report'] = 'sent'
      element.clear()
      time.sleep(4)

new_data.to_excel('out_put/delivery_report_check.xlsx')
print(new_data)
