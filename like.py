from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import Login
import pandas as pd
import time
from pageorusername import check

usr = check()

data = pd.read_excel('/home/lanjithkumar15/programming/kriyamedia/facebook/sample.xls')
for username in data['username']:
    
    driver, res = usr.check_facebook_page_or_id(username)

    if res == 1:
        wait = WebDriverWait(driver, 10)
       
        button1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]"
        button2 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]"
        button3 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]"

        time.sleep(2)
        try:
            button1click = wait.until(EC.element_to_be_clickable((By.XPATH, button1)))
            button1click.click()
        except:
            print("like1 is not found")
        
        try:
            button2click = wait.until(EC.element_to_be_clickable((By.XPATH, button2)))
            button2click.click()
        except:
            print("like2 is not found")
        
        try:
            button3click = wait.until(EC.element_to_be_clickable((By.XPATH, button3)))
            button3click.click()
        except:
            print("like3 is not found")
        
        driver.close()
    
    elif res == 2:

        wait = WebDriverWait(driver, 10)

        button1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]"
        button2 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]"
        button3 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[3]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]"
        try:
            button1click = wait.until(EC.element_to_be_clickable((By.XPATH, button1)))
            button1click.click()
        
        except:
            print("like1 is not found")
        
        try:
            button2click = wait.until(EC.element_to_be_clickable((By.XPATH, button2)))
            button2click.click()
        except:
            print("like2 is not found")
        
        try:
            button3click = wait.until(EC.element_to_be_clickable((By.XPATH, button3)))
            button3click.click()
        except:
            print("like3 is not found")
        
        driver.close()




