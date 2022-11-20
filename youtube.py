from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.youtube.com/")
driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("selenium")
action.key_down(Keys.ENTER).key_up(Keys.ENTER)
action.perform()

time.sleep(10)
driver.close()
driver.quit()
print('searched successfully')