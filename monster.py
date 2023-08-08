import time
#
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
path = (r'C:\Users\veere\Desktop\Python class Assignment\test.doc')
chr=webdriver.ChromeOptions()
chr.add_experimental_option("detach",True)
lanch=webdriver.Chrome(options=chr)
lanch.get("https://www.foundit.in/")

lanch.find_element("xpath",'//input[@type="file"]').send_keys(path)