import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(1000)
driver.maximize_window()
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.get("https://www.geeksforgeeks.org/")
driver.get("https://www.w3schools.com/")
# element = driver.find_element(By.LINK_TEXT,"Contests")
# source_element = driver.find_element(By.ID,"box2")
# target_element = driver.find_element(By.ID,"box106")
action = ActionChains(driver)
# action.click_and_hold(on_element=element)
# action.context_click(on_element=element)
# action.move_by_offset(100, 100).context_click()
# action.click(on_element=element)
# action.double_click(on_element=element)
# action.drag_and_drop(source_element, target_element)
# action.move_to_element(element).click().perform()
# action.move_to_element_with_offset(element,200,300).context_click().perform()

driver.forward()
driver.refresh()

driver.back()

action.perform()


time.sleep(5)
driver.close()
driver.quit()
print('Successful')