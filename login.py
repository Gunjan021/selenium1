import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
driver.implicitly_wait(1000)
driver.get("https://www.languageacademy.com.au/auth/login")
driver.maximize_window()
action = ActionChains(driver)

driver.find_element("name","email").send_keys("gunjan87800@gmail.com")
driver.find_element("name","password").send_keys("Gunjan486526")
# driver.find_element(By.CLASS_NAME,"DuMIQc").click()
driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/section[2]/form/div/div/div[1]/div[4]/button').click()

time.sleep(10)
driver.close()
driver.quit()
print('login Successful')

