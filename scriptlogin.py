from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException



import time
driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.implicitly_wait(30) # This line will cause it to search for 60 seconds

#login 
driver.get("https://www.instagram.com")
driver.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a").click()

#id
username=driver.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[1]/input")
username.clear()
username.send_keys("")

#password
password = driver.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/input")
password.clear()
password.send_keys("")
#time.sleep(5)
driver.find_element_by_xpath(".//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button").click()
