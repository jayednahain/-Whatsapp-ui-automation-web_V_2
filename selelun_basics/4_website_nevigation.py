from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
whats_app_path = 'https://quotes.toscrape.com/'

driver.get(whats_app_path)

"""
   searching structure
('.header-box h1 a')
   <head-box>
      <h1>
         <a>
   """

data = driver.find_element_by_css_selector('.header-box p a')

def log_in_page():
   if data.text == 'Login':
      data.click()

def filed_data():
   name = 'nahian'
   username =driver.find_element_by_css_selector('#username')
   username.send_keys(name)

   password ='123'
   password_data = driver.find_element_by_css_selector('#password')
   password_data.send_keys(password)

def log_in_btn():
   log_in_btn = driver.find_element_by_css_selector('#password')


log_in_page()
time.sleep(2)
filed_data()
