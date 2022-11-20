import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(1000)
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()

driver.find_element("name","username").send_keys("admin@gmail.com")
driver.find_element("name","password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"_acap").click()

time.sleep(5)
driver.close()
driver.quit()
print('Successful')