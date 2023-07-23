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
        time.sleep(5)

        first_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div')))
        first_click.click()

        second_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')))
        second_click.click()
        second_click.clear()
        second_click.click()
        second_click.send_keys(text)
        second_click.send_keys(Keys.RETURN)
        driver.close()

    elif res == 2:
        time.sleep(5)

        first_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div')))
        first_click.click()

        second_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')))
        second_click.click()
        second_click.clear()
        second_click.click()
        second_click.send_keys(text)
        second_click.send_keys(Keys.RETURN)
        driver.close()
