#coding: utf-8
__author__ = 'pkf'

from selenium import webdriver
import time,os,sys
import unittest,random
from selenium.webdriver.support.ui import Select

class Automatic_Bid(unittest.TestCase):

    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        global browser
        browser = webdriver.Chrome(chrome_options=options)
        browser.implicitly_wait(10.0)

        global f
        f = open('./Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'a+')

    

    def logInCnaidai(self):

        def asdfgh(numb):
            print >> f, '【%s】-->:%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')),numb)
            print(numb)
        
        browser.get("http://a.cnaidai.com/webjr/login.htm")
        print ("---->: Come_to_Cnaidai_loginPage")
        asdfgh('1111111111111')
        # stepNum += 1
        time.sleep(1)

        print("---->: Start to input userMessage")
        asdfgh('2222222222222')
        usernameLabel = browser.find_element_by_name("username")
        usernameLabel.clear()
        usernameLabel.send_keys("18267175336")
        print("---->: input username")
        asdfgh('3333333333333')
        time.sleep(1)
        passwordLabel = browser.find_element_by_name("password")
        passwordLabel.clear()
        passwordLabel.send_keys("a1111111")
        print("---->: input password")
        asdfgh('4444444444444')
        time.sleep(1)
        valicodeLabel = browser.find_element_by_name("valicode")
        valicodeLabel.clear()
        valicodeLabel.send_keys("1111")
        print ("---->: input valicode")
        asdfgh('5555555555555')
        time.sleep(1)
        browser.find_element_by_id("login_submit").click()
        print ("---->: Log_into_Cnaidai")
        asdfgh('6666666666666')
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Automatic_Bid('logInCnaidai'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
    f.close()
