from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
element = driver.find_element(By.PARTIAL_LINK_TEXT,"Contests")
print(element)
time.sleep(5)
driver.close()
driver.quit()
print('Successful')
