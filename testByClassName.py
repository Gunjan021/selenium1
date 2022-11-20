import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(1000)
driver.get("http://localhost:3000/Login")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"input1").send_keys("admin@gmail.com")
driver.find_element(By.CLASS_NAME,"input2 ").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"btnlogin").click()

# driver.find_element_by_xpath("//input[@class='input form-control form-control-lg']")
# driver.find_element_by_xpath("//input[@class='password form-control form-control-lg']")
# driver.find_element_by_xpath("//button[@class='btn btn-primary btn-lg']").click()


# driver.find_element(By.cssSelector("input[className='input form-control form-control-lg']"))
# driver.find_element(By.cssSelector("input[className='password form-control form-control-lg']"))
# driver.find_element(By.cssSelector("button[className='btn btn-primary btn-lg']")).click()

time.sleep(10)
driver.close()
driver.quit()
print('Successful')