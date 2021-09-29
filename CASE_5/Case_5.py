from selenium import webdriver
import time
import pandas as pd

option = webdriver.ChromeOptions()

option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe', options=option)
whats_app_path = 'https://web.whatsapp.com/'
driver.get(whats_app_path)



lock = 5

data = int(input("unlock !: "))
if lock == data:
   time.sleep(1)
   dot = driver.find_element_by_xpath('//span[@data-testid="menu"]')
   dot.click()
   time.sleep(2)
   #log_out = driver.find_element_by_xpath('//div[@aria - label="Log out"]')
   #log_out = driver.find_element_by_css_selector('._2oldI')
   #[aria - label = "Log out"]

   log_out = driver.find_element_by_xpath('(//li[@class="_2qR8G _1wMaz _18oo2"])[5]')
   time.sleep(1)

   log_out.click()

   #tab_data = driver.find_elements_by_css_selector('._1HnQz') #_1HnQz
   #driver.switch_to_frame()
   #print(tab_data)

   #log_out.click()




