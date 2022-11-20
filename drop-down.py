from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("D:/Play-Ground/selenium/upload.html")

sel = Select(driver.find_element(By.XPATH,"//*[@id='cars']"))
# sel.select_by_visible_text("Saab")
sel.select_by_index(3)
time.sleep(5)
driver.close()
driver.quit()
print('Successful')