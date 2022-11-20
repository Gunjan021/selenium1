from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome()
driver.get("file:///D:/Play-Ground/selenium/find-elements.html")
alert = Alert(driver)
print(alert.text)
alert.dismiss()
alert.accept()
time.sleep(5)
driver.close()
driver.quit()
print('success')