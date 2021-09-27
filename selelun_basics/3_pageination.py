from selenium import webdriver

driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
whats_app_path = 'https://quotes.toscrape.com/'

driver.get(whats_app_path)



while True:
   """printing data from page"""
   for div in driver.find_elements_by_css_selector('.quote'):
      print(div.find_element_by_css_selector('.text').text)
      print(div.find_element_by_css_selector('.author').text)
      print("----------------------------------------------")


   """afetr printing all the single page data the butoon will click"""
   """if we end of the page there will be create an exception"""
   """so we are using try and except block"""
   try:
      button = driver.find_element_by_class_name('next a').click()
   except:
      print("sorry no more data here !")
      break
