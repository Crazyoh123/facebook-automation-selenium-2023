from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from login import Login
import pandas as pd
import time
from pageorusername import check

usr = check()

text = "hi i am kyri here"

data = pd.read_excel('/home/lanjithkumar15/programming/kriyamedia/facebook/sample.xls')
for username in data['username']:
    driver, res = usr.check_facebook_page_or_id(username)

    if res == 1:
        wait = WebDriverWait(driver, 10)
        comment = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/form/div/div[1]/div[1]/div/div[1]/p"
        
        elementkey = wait.until(EC.element_to_be_clickable((By.XPATH, comment)))
        elementkey.click()
        elementkey.clear()
        elementkey.click()
        elementkey.send_keys(text)
        elementkey.send_keys(Keys.RETURN)
        driver.close()
        
    elif res == 2:
        
        wait = WebDriverWait(driver, 10)
        xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/form/div/div[1]/div[1]/div/div[1]/p"

        elementkey = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elementkey.click()
        elementkey.clear()
        elementkey.click()
        elementkey.send_keys(text)
        elementkey.send_keys(Keys.RETURN)
        driver.close()