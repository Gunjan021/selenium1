from selenium import webdriver
import time
# from PIL import Image
driver = webdriver.Chrome()
url = "https://www.geeksforgeeks.org/"
driver.get(url)
driver.maximize_window()
driver.save_screenshot("image.png")
# image = Image.open("image.png")
# image.show()
time.sleep(3)
driver.close()
driver.quit()
print('success')
