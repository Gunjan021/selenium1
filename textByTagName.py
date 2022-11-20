import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# driver.implicitly_wait(1000)
driver.get("http://localhost:3000/Login")
driver.maximize_window()

driver.find_element(By.TAG_NAME,'P')
driver.find_element(By.TAG_NAME,'div')

time.sleep(5)
driver.close()
driver.quit()
print('Successful')