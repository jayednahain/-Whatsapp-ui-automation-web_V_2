from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe',options=option)
#driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
whats_app_path = 'https://web.whatsapp.com/'

driver.get(whats_app_path)


lock = 5

data = int(input("unlock !: "))

if data==lock:
   #value = "nahian"
   #search_box = driver.find_element_by_class_name('_1Jn3C')
   #select_data = driver.find_element_by_css_selector('.textbox').text

   search_box = driver.find_element_by_class_name('_3Qnsr').text
   print(search_box)
   #data = "nahian"
  #search_box.send_keys(data)



   #search_box.send_keys(value)
   #print(search_box)


else:
   pass
