# import the libs
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
# create the initial window
driver = webdriver.Chrome()
driver.maximize_window()
# go to the home page
driver.get('https://www.zomato.com')

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

# wait for page to load completely

# click on the sign in tab
driver.find_element(By.XPATH,'//*[@id="navigation_clalxhlde001m1jlp6nwb3he4"]/li[4]/a').click()

time.sleep(5)

# click to log in using facebook

driver.find_element(By.XPATH,'//*[@id="id-58"]/section[2]/section/div[4]/div/span').click()

# changing the handles to access login page
for handle in driver.window_handles:
	if handle != main_page:
		login_page = handle
		
# change the control to signin page		
driver.switch_to.window(login_page)

# user input for email and password
print('Enter email id : ', end ='')
email = input().strip()
print('Enter password : ', end ='')
password = input().strip()

# enter the email
driver.find_element_by_xpath('//*[@id ="email"]').send_keys(email)

# enter the password
driver.find_element_by_xpath('//*[@id ="pass"]').send_keys(password)

# click the login button
driver.find_element_by_xpath('//*[@id ="u_0_0"]').click()



# change control to main page
driver.switch_to.window(main_page)

time.sleep(10)
# print user name
name = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/header/div[2]/div/div/div/div/span').text
print('Your user name is : {}'.format(name))

# closing the window
time.sleep(5)
driver.close()
driver.quit()
print('success')
