from selenium import webdriver

driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
whats_app_path = 'https://quotes.toscrape.com/'

driver.get(whats_app_path)


"""using CSS slector"""
#driver.find_element_by_css_selector('.next a').click()
#if we wnat to click button! always refer ancor tag after class tag




#change page by button click
number = 5
for i in range(number):
   button = driver.find_element_by_class_name('next a')
   button.click()