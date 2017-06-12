#coding: utf-8
__author__ = 'pkf'

from selenium import webdriver
from time import sleep
import traceback
import time
import sys
import random
import re
import my

def startToRegister():
    registerCnAiDai('', '', '')
    registerCnAiDai('123', '', '')
    registerCnAiDai('kkk', '', '')
    registerCnAiDai('i9jhg66redd49', '', '')
    registerCnAiDai('yg9-80[;;'';87', '', '')
    registerCnAiDai('11111111111', '', '')
    registerCnAiDai('12522223333', '', '')
    registerCnAiDai('18267175336', '', '')
    registerCnAiDai('18258173861', '', '')

    for i in range(1, 10):
        #随机选取手机号码
        phone = random.choice(['13', '18', '14', '17', '15']) + "".join(random.choice("0123456789") for i in range(9))
        registerCnAiDai(phone, '', '')

def registerCnAiDai(phoneNum, passWd, inviteUser):

    sleep(1)
    checkUserName(phoneNum, passWd, inviteUser)

    checkValicode()

    checkMessageBtn()

    phoneCode = input('请手动输入手机验证码：')
    checkPhoneCode(phoneCode)

    checkPassWord(passWd)

def checkUserName(phoneNum, passWd, inviteUser):
    print >> f, '【%s】 ======================================手机号验证开始========================================' % (str(time.strftime('%Y_%m_%d %H:%M:%S')))
    userNameLabel = browser.find_element_by_name('userName')
    userNameLabel.clear()
    userNameLabel.send_keys(phoneNum)
    browser.find_element_by_css_selector('body > div.reg-bg > div.frame-bg > div.reg-input-box > h2').click()
    sleep(1)

    regex1 = "^1(3|4|5|7|8)\d{9}$"
    match1 = re.search(regex1, "%s" % phoneNum)

    if match1:  # 对的选项
        try:
            browser.find_element_by_css_selector('#reg_msg > span:nth-child(1)')
            txt = browser.find_element_by_css_selector('#reg_msg > span:nth-child(1)').text
            while txt == '':
                txt = '手机号符合'
            print >> f, '【%s】 register( %s , %s , %s )  %s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum, passWd, inviteUser, txt)
            if txt == '该手机号已经被注册,请更换手机号':
                print '手机号：（', phoneNum, '):', txt
                print >> f, '【%s】 手机号:( %s ) %s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum, txt)
                print '手机号验证逻辑与平台相同', match1
                print >> f, '【%s】 %s 手机号验证逻辑与平台相同' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum)
                return
            elif txt == '手机号符合':
                print '手机号：（', phoneNum, '):', txt
                print >> f, '【%s】 手机号:( %s ) %s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum, txt)
                print '手机号验证逻辑与平台相同', match1
                print >> f, '【%s】 %s 手机号验证逻辑与平台相同' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum)
            else:
                print '手机号验证（平台）逻辑错误', match1
                print >> f, '【%s】 %s 手机号验证（平台）逻辑错误' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum)
                return
        except:
            print '手机号：（', phoneNum, '):手机号符合'
            print >> f, '【%s】 手机号:( %s ) ：手机号符合' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum)
            print '手机号验证逻辑与平台相同', match1
            print >> f, '【%s】 %s 手机号验证逻辑与平台相同' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum)
    else:  # 错的选项
        try:
            browser.find_element_by_css_selector('#reg_msg > span:nth-child(1)')
            txt = browser.find_element_by_css_selector('#reg_msg > span:nth-child(1)').text
            print >> f, '【%s】 register( %s , %s , %s ) %s ' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum, passWd, inviteUser, txt)
            print '手机号：（', phoneNum, '):', txt
            print '手机号验证逻辑与平台相同', match1
            print >> f, '【%s】 %s 手机号验证逻辑与平台相同' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum)
            return
        except:
            print '手机号验证（平台）逻辑错误', match1
            print >> f, '【%s】 %s 手机号验证（平台）逻辑错误' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneNum)
            return

    print '手机号校验完成'
    print >> f, '【%s】 ======================================手机号验证结束========================================' % (str(time.strftime('%Y_%m_%d %H:%M:%S')))

def checkPhoneCode(phoneCode):
    print >> f, '【%s】 ======================================手机验证码验证开始========================================' % (str(time.strftime('%Y_%m_%d %H:%M:%S')))
    browser.find_element_by_class_name('phoneCode').send_keys(phoneCode)

    regex3 = "^\d{6}$"
    match3 = re.search(regex3, "%s" % '852963')
    if match3:  ##错的选项
        print '验证码内容不符合规定：', phoneCode
        print >> f, '【%s】验证码内容不符合规定: %s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneCode)
        return
    else:  # 对的选项
        print '验证码内容符合规定：', phoneCode
        print >> f, '【%s】验证码内容符合规定: %s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), phoneCode)
    print >> f, '【%s】 ======================================手机验证码验证结束========================================' % (str(time.strftime('%Y_%m_%d %H:%M:%S')))

def checkPassWord(passWd):
    print >> f, '【%s】 ======================================密码验证开始========================================' % (str(time.strftime('%Y_%m_%d %H:%M:%S')))
    browser.find_element_by_name('password').send_keys(passWd)
    if len(passWd) < 17 and len(passWd) > 7:
        regex2 = re.compile('([^a-z0-9A-Z])+')
        match2 = regex2.findall(passWd)
        if match2:
            print '密码内容不符合规定：', passWd
            print >> f, '【%s】密码内容不符合规定: %s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), passWd)
            return
        else:
            print '密码内容符合规定：', passWd
            print >> f, '【%s】密码内容符合规定: %s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), passWd)
    else:
        print '密码位数不符合规定: ', passWd
        print >> f, '【%s】密码位数不符合规定: %s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), passWd)
        return
    print >> f, '【%s】 ======================================密码验证结束========================================' % (str(time.strftime('%Y_%m_%d %H:%M:%S')))

def check():
    browser.find_element_by_name('valicode').send_keys('1111')
    try:
        txt = browser.find_element_by_css_selector('# reg_msg > span:nth-child(2)').text
        print >> f, '【%s】%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), txt)
        return
    except:
        print 'valicode meet_to_criteria

def checkMessageBtn():
    try:
        browser.find_element_by_name('valcode').click()
    except:
        print >> f, '【%s】%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), '===================================================================')
        traceback.print_exc(file=f)
        print >> f, '【%s】%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), '===================================================================')
        f.flush()
        f.close()
        print '已出错 registerCnAiDai(\%s, \%s, \%s)', phoneNum, passWd, inviteUser
        return

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    global browser
    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(10.0)
    global f
    f = open('./Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'a+')
    browser.get('https://pc.cnaidai.com/webpc/register.htm')
    startToRegister()
    browser.quit()