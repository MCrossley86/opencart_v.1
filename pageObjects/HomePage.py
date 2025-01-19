from selenium.webdriver.common.by import By

class HomePage():
    lnk_myaccount_xpath = "//a[normalize-space()='My Account']"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"

    def __init__(self, driver):
        self.a_driver = driver
    def clickMyAccount(self):
        self.a_driver.find_element(By.XPATH,self.lnk_myaccount_xpath).click()
    def clickRegister(self):
        self.a_driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()
    def clickLogin(self):
        self.a_driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
