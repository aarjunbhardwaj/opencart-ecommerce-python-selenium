from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    NoSuchElementException
)


class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.my_account_xpath = '//span[text()="My Account"]'
        self.register_xpath = ".//ul//a[text()='Register']"
        self.login_xpath = '//a[text()="Login"]'
    
    def scroll_to_element(self,element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(0.5)


    def click_my_account(self):
            
                my_account_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.my_account_xpath))
                )
                self.scroll_to_element(my_account_element)
                my_account_element.click()

        
    def click_register(self):
            
            register_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.register_xpath))
            )
            self.scroll_to_element(register_element)
            register_element.click()
           
 
    def click_login(self):
        login_element = self.driver.find_element(By.XPATH,self.login_xpath)
        self.scroll_to_element(login_element)
        login_element.click()



