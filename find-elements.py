import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(1000)
driver.get("file:///D:/Play-Ground/selenium/find-elements.html")
driver.maximize_window()
elements = driver.find_elements(By.TAG_NAME,'input')
print(len(elements))
time.sleep(5)
driver.close()
driver.quit()
print('Successful')