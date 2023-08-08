import time

from selenium import webdriver
chr= webdriver.ChromeOptions()
chr.add_experimental_option("detach",True)
drive = webdriver.Chrome(options=chr)
drive.implicitly_wait(20)
dr=drive.get("https://www.shoppersstack.com/")
#drive.implicitly_wait(50)
#drive.find_element("xpath",'//button[@id="loginBtn"]').click()
#login=drive.find_element("id","loginBtn")
drive.find_element("css selector",'button[name="loginBtn"]').click()
drive.find_element("css selector",'span[class="MuiButton-label"]').click()
drive.find_element('id',"Create Account").click()


drive.find_element('id',"First Name").send_keys("veeresj")

#drive.find_element('id',"Email").send_keys("veeresh@gmail.com")
drive.find_element()

time.sleep(30)
drive.close()



