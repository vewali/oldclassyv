import time
#
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

chr=webdriver.ChromeOptions()
chr.add_experimental_option("detach",True)
lanch=webdriver.Chrome(options=chr)
#
lanch.get("https://www.myntra.com/?")
#lanch.find_element("xpath",'//div(@data-group="men")')
action = ActionChains(lanch)
lanch.implicitly_wait(30)
man= lanch.find_element("xpath",'(//a[text()="Men"])[1]')
action.move_to_element(man).perform()
time.sleep(2)
shart=lanch.find_element("xpath",'(//a[text()="Sweatshirts"])[1]')
#action.move_to_element(shart).perform()
time.sleep(2)
shart.send_keys(Keys.ENTER)
#
#time.sleep(10)
#lanch.close()

action.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL)


# dri = webdriver.Chrome()
# dri.get("https://www.flipkart.com/")
# time.sleep(3)
# electronics= ActionChains(dri)
# time.sleep(3)
# el_obj=dri.find_element("xpath", '//span[text()="Electronics"]')
# time.sleep(3)
# electronics.move_to_element(el_obj).perform()
# time.sleep(3)
# sub_el=dri.find_element("xpath", '//a[text()="Desktop PCs"]')
# time.sleep(3)
# electronics.move_to_element(sub_el).perform()
# time.sleep(3)