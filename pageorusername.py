from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from login import Login
import pandas as pd
import time

class check():
    def check_facebook_page_or_id(self,username):
       log = Login()
       driver = log.login()
       
       time.sleep(5)
       driver.get(f"https://www.facebook.com/{username}")
       
       time.sleep(5)
       
       xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/ul/div[1]/div[1]/img"

       try:
        element = driver.find_element(By.XPATH, xpath)
        return driver, 1 #for page
       except NoSuchElementException:
         return driver, 2 #for user id


