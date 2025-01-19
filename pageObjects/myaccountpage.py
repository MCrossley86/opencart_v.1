from selenium.webdriver.common.by import By

class myaccountpage():

    lnk_logout_xpath = "//aside[@id='column-right]//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()