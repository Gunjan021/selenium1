from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("D:/Play-Ground/selenium/upload.html")
driver.find_element(By.CSS_SELECTOR,"input#file").send_keys("D:/Play-Ground/selenium/image.png")
time.sleep(5)
driver.close()
driver.quit()
print('success')