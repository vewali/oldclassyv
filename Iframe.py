
import time
#
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
#path = (r'C:\Users\veere\Desktop\Python class Assignment\test.doc')
chr=webdriver.ChromeOptions()
chr.add_experimental_option("detach",True)
lanch=webdriver.Chrome(options=chr)
lanch.get("https://www.redbus.in/")
time.sleep(2)
lanch.maximize_window()
lanch.find_element("xpath",'//span[text()="Account"]').click()
a=ActionChains(lanch)
time.sleep(2)
lanch.find_element("xpath",'(//span[@class="header_dropdown_item_name"])[5]').click()
#a.move_to_element(login).perform()
time.sleep(5)
#login = lanch.find_element("id","user_sign_in_sign_up")
#a.move_to_element(login).click()

loginpage=lanch.find_element("xpath",'//iframe[@class="modalIframe"]')
lanch.switch_to.frame(loginpage)
handles = lanch.window_handles
lanch.find_element("xpath",'//input[@type="number"]').send_keys("9916993732")
time.sleep(20)

print(handles)
lanch.find_element("xpath",'//div[@id="otp-container"]').click()

print(handles)
#lanch.switch_to.window(handles[1])
#lanch.find_element("xpath",'//input[@type="text"]').send_keys("011821")
time.sleep(20)
print(handles)
lanch.find_element("xpath",'//button[@id="verifyUser"]').click()


#lanch.find_element("xpath",'//input[@type="number"]').send_keys(9916993732)
# lanch.find_element("xpath",'//iframe[@title="Sign in with Google Button"]').click()

# lanch.switch_to.window(handles[1])
# #lanch.switch_to.new_window()
# lanch.find_element("xpath",'//input[@type="email"]').send_keys("veeresh.b9254@gmail.com")

#lanch.switch_to.new_window(goofgle)

