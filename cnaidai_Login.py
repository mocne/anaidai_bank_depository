#coding: utf-8
__author__ = 'pkf'

from selenium import webdriver
import time,os,sys

def logInCnaidai():
    
    reload(sys)
    sys.setdefaultencoding('utf8')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    global browser
    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(10.0)

    global f
    f = open('./Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'a+')
    browser.get("http://a.cnaidai.com/webjr/login.htm")
    printMe("Come_to_Cnaidai_loginPage")
    sleep(1)

    printMe("Start to input userMessage")
    usernameLabel = browser.find_element_by_name("username")
    usernameLabel.clear()
    usernameLabel.send_keys("18267175336")
    printMe("input username")
    sleep(1)
    passwordLabel = browser.find_element_by_name("password")
    passwordLabel.clear()
    passwordLabel.send_keys("a1111111")
    printMe("input password")
    sleep(1)
    valicodeLabel = browser.find_element_by_name("valicode")
    valicodeLabel.clear()
    valicodeLabel.send_keys("1111")
    printMe("input valicode")
    sleep(1)
    browser.find_element_by_id("login_submit").click()
    printMe("Log_into_Cnaidai")
    sleep(3)

def printMe(words):
            print >> f, '【%s】%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')),words)
            print(words)
