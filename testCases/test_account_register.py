from pageObjects.AccountRegister import AccountRegistrationPage
from pageObjects.HomePage import HomePage
import time

class TestAccountRegistration:


    def test_account_register_001(self,setup):
        self.home_page = HomePage(setup)
        self.home_page.click_my_account()
        self.home_page.click_register()
        self.register_page = AccountRegistrationPage(setup)
        self.register_page.set_firstname("Arjun")
        self.register_page.set_lastname("Bhardwaj")
        self.register_page.set_email("jddscsc@gmail.com")
        self.register_page.set_password("bsdckcdscj")
        self.register_page.set_newsletter()
        self.register_page.set_tc_agree()
        self.register_page.click_continue()
        time.sleep(1)
        confirm_msg = self.register_page.get_confirmation()
        time.sleep(1)
        expected_msgs = ["Your Account Has Been Created!", "Register Account"]
        assert confirm_msg in expected_msgs
                

