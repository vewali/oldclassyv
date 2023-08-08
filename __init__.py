import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
chr=webdriver.ChromeOptions()
chr.add_experimental_option("detach",True)
lanch=webdriver.Chrome(options=chr)

lanch.get("https://www.myntra.com/?")
lanch.find_element("xpath",'//div(@data-group="men")')
action = ActionChains(lanch)
lanch.implicitly_wait(30)

action.move_to_element("xpath",'(//a[text()="Men"])[1]').perform()
action.move_to_element("xpath",'(//a[text()="Sweatshirts"])[1]').perform()

time.sleep(10)
lanch.close()