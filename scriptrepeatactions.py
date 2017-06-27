from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException

import time

count=0
while count < 500:
    try:
        #like
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div/article/div[2]/section[2]/a/span").click()
        actions = ActionChains(driver)
        time.sleep(2)
        #comment
        comment=driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div/article/div[2]/section[2]/form/input")
        comment.send_keys("nice!")
        comment.send_keys(Keys.RETURN)
        time.sleep(2)

        #follow
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div/article/header/span/button").click()
        time.sleep(2)

        #right
        actions.send_keys(Keys.RIGHT).perform()
        count=count+1
        print(count)
    except:
         #like
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div/article/div[2]/section[2]/a/span").click()
        actions = ActionChains(driver)
        time.sleep(2)
        #comment
        comment=driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div/article/div[2]/section[2]/form/input")
        comment.send_keys("nice!")
        comment.send_keys(Keys.RETURN)
        time.sleep(2)
        actions.send_keys(Keys.RIGHT).perform()
        count=count+1
        print(count)
        continue
