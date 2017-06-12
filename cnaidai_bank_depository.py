#coding: utf-8
__author__ = 'pkf'

from selenium import webdriver
import time,os,sys
import unittest,random
from selenium.webdriver.support.ui import Select
import cnaidai_Login

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

    def startTest(self):
        printMe('start to test')
        cnaidai_Login.logInCnaidai()

def printMe(words):
            print >> f, '【%s】%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')),words)
            print(words)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Automatic_Bid('startTest'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
    f.close()
