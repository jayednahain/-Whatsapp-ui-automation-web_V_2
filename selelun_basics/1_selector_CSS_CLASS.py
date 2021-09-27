from selenium import webdriver

driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
whats_app_path = 'https://quotes.toscrape.com/'

driver.get(whats_app_path)





#using class
# for div in driver.find_elements_by_class_name('quote'):
#    print(div.find_element_by_class_name('text').text)
#    print(div.find_element_by_class_name('author').text)
#    print("---------------------------------")


#using CSS
for div in driver.find_elements_by_css_selector('.quote'):
   print(div.find_element_by_css_selector('.text').text)
   print(div.find_element_by_css_selector('.author').text)
   print("---------------------------------")