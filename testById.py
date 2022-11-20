from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/")
element = driver.find_element(By.LINK_TEXT,"Videos")
action = ActionChains(driver)
action.click(on_element = element)
action.release(on_element = element)
action.perform()
time.sleep(5)
driver.close()
driver.quit()
print('Successful')