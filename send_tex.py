from selenium import webdriver
import time

option = webdriver.ChromeOptions()

option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe',options=option)
whats_app_path = 'https://web.whatsapp.com/'

driver.get(whats_app_path)

#define function which will get massange information
def massege():
   name    = input('Enter user name: ')
   content = input('enter text content: ')
   count   = int(input('how manay times you want to send ?: '))

   user_name_div = driver.find_element_by_xpath(
      '//span[@title="{}"]'.format(name)
   )

   #clicking the user name button for open up window
   user_name_div.click()
   time.sleep(4)

   send_data_box = driver.find_element_by_class_name('p3_M1')
   #send_data_box.send_keys(".")

   for i in range(count):
      send_data_box.send_keys(content)
      driver.find_element_by_class_name('_4sWnG').click()
      time.sleep(2)



massege()

def warnings():
   print("do you want to send more massange? Y or N ")
   ask_user = input("press y or N")
   if (ask_user=='Y' or ask_user=='y'):
      massege()
      warnings()

   elif (ask_user =='n' or ask_user=='N'):
      print("thank you")
   else:
      print('please enter a valied option')
      warnings()


warnings()
