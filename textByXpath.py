import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(1000)
driver.get("http://localhost:3000/Login")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='form3Example3']").send_keys("admin@gmail.com");
driver.find_element(By.XPATH,"//input[@id='form3Example4']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@id='buttonlogin']").click()

time.sleep(10)
driver.close()
driver.quit()
print('Successful')
