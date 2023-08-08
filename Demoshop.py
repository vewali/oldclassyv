
import time

from  selenium import webdriver
chr= webdriver.ChromeOptions()
chr.add_experimental_option("detach",True)
launch_chome = webdriver.Chrome(options= chr)
url = "https://demowebshop.tricentis.com/"
launch_chome.get(url)
launch_chome.fullscreen_window()
time.sleep(2)
register= launch_chome.find_element("link text","Register")
register.click()
launch_chome.fullscreen_window()
Gender=launch_chome.find_element("id","gender-male")
female= launch_chome.find_element("id","gender-female")
time.sleep(1)
if Gender.is_selected() == False or female.is_selected() == False:
 Gender.click()
 time.sleep(2)
first_name =launch_chome.find_element("id","FirstName")
first_name.send_keys("veer")
last_name =launch_chome.find_element("id","LastName")
last_name.send_keys("python")
mail=launch_chome.find_element("id","Email")
mail.send_keys("radj3iw2261391s@gmail.com")
password=launch_chome.find_element("id","Password")
password.send_keys("password@123")
confrim_password=launch_chome.find_element("id","ConfirmPassword")
confrim_password.send_keys("password@123")
submit=launch_chome.find_element("id","register-button")
submit.click()
launch_chome.fullscreen_window()
time.sleep(2)
logout=launch_chome.find_element("class name","ico-logout")
logout.click()
launch_chome.fullscreen_window()


launch_chome.close()
