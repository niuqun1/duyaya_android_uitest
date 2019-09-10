"""

======================

@author:niuqun

@time:2019/9/4:10:36 AM

@email:17689551930@163.com

======================

"""
from selenium.webdriver.common.by import By
import Page
import allure
from Base.Base import Base
import sys,os
sys.path.append(os.getcwd())
from  time import sleep
class search(Base):
    def  __init__(self,deiver):
        Base.__init__(self,deiver)
    # 点击手机号登陆
    def click_login(self):
        self.click_element(Page.phone_login)
    # 微信登陆
    def click_wx_lojin(self):
        self.click_element(Page.wx_login)
        # mylogger.info("微信登陆")
    # 杜丫丫隐私安全yes
    def click_duyaya_privacy(self):
        self.click_element(Page.privacy_yes)
    # 杜丫丫隐私安全no
    # def click_duyaya_privacy_no(self):
    #     self.click_element(Page.privacy_no)
    # 获取ios跳转权限
    def click_system(self):
        self.click_element(Page.system_ios)
    # 课堂type
    def click_classroom(self):
        self.click_element(Page.classroom)
        # mylogger.info("点击课堂")
    # 点击如何上课
    def click_who_word(self):
        self.click_element(Page.who_word)
        # mylogger.info("进入如何让上课")
    # 下载课程
    def click_download(self):
        self.click_element(Page.download)
        # mylogger.info("课程下载")
        sleep(4.5)
    #点击I'm hungry
    def click_hungry(self):
        self.click_element(Page.hungry)
        # mylogger.info("进入hungry课程")
    # 循环进入关卡然后退出
    def for_a(self,customs_list):
        for customs in customs_list:
            By_name=(By.XPATH,'//*[@text="%s"]'%customs)
            self.click_element(By_name)
            # mylogger.info("进入%s"%customs)
            sleep(3)
            self.driver_reset()
            sleep(2)
            self.slide(234,300,200,164,1000)
            sleep(0.5)
    # 进入picnic
    def click_picnic(self):
        self.click_element(Page.pinnic)
        # mylogger.info("进入picnic课程")
    # 进入What_this
    def click_what_rhis(self):
        self.click_element(Page.What_this)
        # mylogger.info("进入What_this课程")

    # 进入onthefarm
    def click_on_the_farm(self):
        self.click_element(Page.on_the_farm)
        # mylogger.info("进入onthefarm课程")
    # 进入review
    def click_review(self):
        self.click_element(Page.review)
        # mylogger.info("进入review课程")
        self.click_element(Page.download)
        # mylogger.info("下载reciew")
        sleep(4)
        self.click_element(Page.reviews)
    # 点击我的
    def click_my(self):
        self.click_element(Page.my)
        # mylogger.info("进入我的页面")
    # 点击杜丫丫
    def click_duyaya(self):
        self.click_element(Page.duyaya)
        # mylogger.info("进入杜丫丫页面")
    # 点击发现
    def click_discover(self):
        self.click_element(Page.discover)
        # mylogger.info("进入发现页面")
    # 发现——如何让上课
    def click_discover_woy(self):
        self.click_element(Page.how_clss)
        # mylogger.info("进入发现如何上课")
    # 点击练习客服
    def click_linkman(self):
        self.click_element(Page.relation)
        # mylogger.info("进入发现页面联系客服")
    # 购买课程点击课程
    def click_buy_customs(self):
        self.click_element(Page.buy_cou)
        # mylogger.info("进入发现页面购买课程")
    def click_add(self):
        self.click_element(Page.Add_the_address)
        # mylogger.info("进入添加地址页面")
    def click_call(self):
        self.click_element(Page.call)

    def  click_retur(self):
        self.click_element(Page.return_duyaya)
        # mylogger.info("发现页如何上课返回 按钮")
    def click_add_return(self):
        self.click_element(Page.add_return)
        # mylogger.info("购买课返回返回 按钮")
    def click_return(self):
        self.click_element(Page.return_lict)
        # mylogger.info("课程内部返回 按钮")





