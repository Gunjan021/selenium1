from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.instagram.com/accounts/login/")

action = ActionChains(driver)

action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

time.sleep(20)
driver.close()
driver.quit()
print('Successful')