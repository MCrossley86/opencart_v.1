from selenium.webdriver.common.by import By

class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_password = "password"
    chk_policy_name = "agree"
    btn_click_xpath = "//button[normalize-space()='Continue']"
    text_msg_conf_xpth = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.b_driver = driver
    def scrllbottom(self):
        self.b_driver.execute_script("window.scrollTo(0, 1040)")
    def setFirstName(self,fname):
        self.b_driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)
    def setLastName(self,lname):
        self.b_driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)
    def setEmail(self,email):
        self.b_driver.find_element(By.NAME,self.txt_email_name).send_keys(email)
    def setPassword(self,pwd):
        self.b_driver.find_element(By.NAME,self.txt_password).send_keys(pwd)
    def setPrivacyPolicy(self):
        self.b_driver.find_element(By.NAME,self.chk_policy_name).click()
    def clickContinue(self):
        self.b_driver.find_element(By.XPATH,self.btn_click_xpath).click()
    def getconfirmationmsg(self):
        try:
            return self.b_driver.find_element(By.XPATH,self.text_msg_conf_xpth).text
        except:
            None
