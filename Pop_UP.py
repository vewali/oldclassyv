import time
#
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
path = (r'C:\Users\veere\Desktop\Python class Assignment\test.doc')
chr=webdriver.ChromeOptions()
chr.add_experimental_option("detach",True)
lanch=webdriver.Chrome(options=chr)
lanch.get("https://nxtgenaiacademy.com/alertandpopup")
#lanch.find_element("xpath",'//button[@name="alertbox"]').click()
#lanch.find_element("xpath",'//button[@name="confirmalertbox"]').click()
lanch.find_element("xpath",'//button[@name="promptalertbox1234"]').click()
alert =Alert(lanch)
time.sleep(2)
alert.send_keys("No")
alert.dismiss()