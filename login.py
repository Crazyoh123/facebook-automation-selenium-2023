from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Login:
    def login(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.facebook.com/login/')

        username = "lanjithkumar15@gmail.com"
        password = "Lanjith15$"

        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input'))
        )
        password_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input')
        login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[3]/button')

        username_input.send_keys(username) 
        password_input.send_keys(password) 

        login_button.click()

        WebDriverWait(driver, 10).until(EC.title_contains('Facebook'))

        return driver
    