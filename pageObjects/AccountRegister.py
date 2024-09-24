import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class AccountRegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.firstname_id = "input-firstname"
        self.lastname_id = "input-lastname"
        self.email_id = "input-email"
        self.phone_id = "input-telephone"
        self.password_id = "input-password"
        self.confirm_password_id = "input-confirm"
        self.newsletter_yes_xpath = '//label[text()="Yes"]/input[@type="radio"]'
        self.term_condition_css_selector = 'input[type="checkbox"]'
        self.continue_bttn_css_selector = 'input[type="submit"]'
        self.confirm_msg_css_selector = 'div[id="content" ]>h1'

    def set_firstname(self, fname):
        fname_element = self.driver.find_element(By.ID, self.firstname_id)
        fname_element.send_keys(fname)
        
    def set_lastname(self, lname):
        lname_element = self.driver.find_element(By.ID, self.lastname_id)
        lname_element.send_keys(lname)

    def set_email(self, email):
        email_element = self.driver.find_element(By.ID, self.email_id)
        email_element.send_keys(email)

    def set_phone(self,phone):
        phone_element = self.driver.find_element(By.ID,self.phone_id)
        phone_element.send_keys(phone)

    def set_password(self, password):
        password_element = self.driver.find_element(By.ID, self.password_id)
        password_element.send_keys(password)

    def set_newsletter(self):
        self.driver.find_element(By.XPATH, self.newsletter_yes_xpath).click()

    def set_tc_agree(self):
        self.driver.find_element(By.CSS_SELECTOR, self.term_condition_css_selector).click()
   
    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.continue_bttn_css_selector).click()

    def get_confirmation(self):
        confirm_msg_element = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, self.confirm_msg_css_selector))
            )
        return  confirm_msg_element.text
    
    