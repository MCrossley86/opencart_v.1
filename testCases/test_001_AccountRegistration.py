from pageObjects.HomePage import HomePage
from pageObjects.AccountsRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.readProperties import readconfig
from utilities.customLogger import LogGen
import os
import time

class Test_001_AccountReg:
    baseURL = readconfig.getapplicationurl()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("*** test_001_AccountRegistration started ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("*** test_001_AccountRegistration launching application ***")
        self.driver.maximize_window()
        time.sleep(8)

        self.hp=HomePage(self.driver)
        self.logger.info("*** test_001_AccountRegistration clicking on my account and registering ***")
        self.hp.clickMyAccount()
        time.sleep(8)
        self.hp.clickMyAccount()
        time.sleep(8)
        self.hp.clickRegister()

        self.regpage=AccountRegistrationPage(self.driver)
        self.logger.info("*** test_001_AccountRegistration entering personal details ***")
        self.regpage.scrllbottom()
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Candy")
        self.email=randomeString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("adF1")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("*** test_001_AccountRegistration passed ***")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png") #(filename="..\\screenshots\\test_account_reg.png")
            self.logger.error("*** test_001_AccountRegistration failed ***")
            self.driver.close()
            assert False
        self.logger.info("*** test_001_AccountRegistration completed ***")

