from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
option = webdriver.ChromeOptions()
option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
#driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe')
#whats_app_path = 'https://web.whatsapp.com/'


# Replace below path with the absolute path
browser = webdriver.Chrome('WebDriver/chromedriver.exe',options=option)

phone = "+8801776-000998"
message = "Hellow"

url = "https://web.whatsapp.com/send?phone="+ phone + "&text=" + message + "&app_absent=1"

# Load Whatsapp Web page
browser.get(url)

# Wait for the page be loaded


enter_action = ActionChains(browser)
enter_action.send_keys(Keys.ENTER)

# Send message
enter_action.perform()

# Close browser
