import configparser
import os
from fileinput import filename

config = configparser.RawConfigParser()
#config.read(filenames="..\\configurations\\config.ini")
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class readconfig():
    @staticmethod
    def getapplicationurl():
        url=config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getuseremail():
        username=config.get('commonInfo','email')
        return username

    @staticmethod
    def getpassword():
        password=config.get('commonInfo', 'password')