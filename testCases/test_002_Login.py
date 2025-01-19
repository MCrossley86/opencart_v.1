import pytest

from pageObjects.HomePage import HomePage
from pageObjects.loginpage import loginpage
from utilities.readProperties import readconfig
from utilities.customLogger import LogGen
import os

class test_login():
    baseURL = readconfig.getapplicationurl()
    logger = LogGen.loggen()

    user = readconfig.getuseremail()
    password = readconfig.getpassword()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*** test_002_test_login started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = loginpage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots"+"test_login.png")
            assert False

        self.driver.close()
        self.logger.info("### end of test login...###")