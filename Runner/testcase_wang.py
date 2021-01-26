from SourceCode.LoginMode import Login
from SourceCode.PaymentProcessMode import PayMode
from tools.basic import Basic
# from ddt import ddt, data, unpack

# import unittest
import pytest
import time
import csv
import random

def getCsvData(filepath):
    list = []
    f = open(filepath, encoding='UTF-8')
    next(f)
    r = csv.reader(f)
    for temp in r:
        list.append(temp)
    return list
#
# def getPagePath(filepath):
#     f = open(filepath, encoding='UTF-8')
#     next(f)
#     r = csv.reader(f)
#     print(r)
#     l=[]
#     for temp1 in r:
#         # print(r.line_num)
#         l.append(temp1)
#     return len(l)

csvDataCode = getCsvData(r"D:\lovesgou\testcase\CodeTest.CSV")
csvDataID = getCsvData(r"D:\lovesgou\testcase\IDPasswordTest.CSV")
# path = r"D:\lovesgou\LoginMod\testcase\PagePath.CSV"
path1=r"D:\lovesgou\testcase\CodeTest.CSV"

# @ddt
class MyTestCase(object):
    # @classmethod
    def __init__(self):
        self.a = Basic()    # 基本工具类的实例化对象
        self.b = Login(self.a)    # 登录页面操作的实例化对象
        self.c = PayMode(self.a)    # 支付流程模块的实例化对象
        self.a.openWeb("http://demo.lovesgou.com/")

    def test_CodeLoginSeccess(self):
        value_ID = "13000000000"
        value_Pwd = "8888"
        self.b.jumopCodeLoginMod()
        self.b.codeIDLoginMod(value_ID)
        self.b.codePasswordLoginMod(value_Pwd)
        self.b.codeLoginBtn()
        # !-----------------------------------------------断言---------------------------------------------! #
        self.eleText_01 = self.a.findElementTextSection("xpath", self.b.xpathHomePageId, 4)
        self.eleText_02 = value_ID[len(value_ID) - 4:]
        if self.eleText_01 == self.eleText_02:
            print("断言成功，01")
            self.c.chooseWares()
            self.c.clickWare()
            # self.c.ranNomsBtn()
            self.c.joinShopCar()
            self.c.goShopCarSett()
            self.c.allCheckBox()
            self.c.goSett()
            self.c.addConsigneeAddr(self.a.phoneNORandomGenerator("word"),
                                    self.a.phoneNORandomGenerator("phone"),
                                    self.a.phoneNORandomGenerator("word"))
            time.sleep(3)
            self.c.windowScrrollBy()
            self.c.placeOrder()
            self.c.balancePaySendCode()
            self.c.backstage()
            self.c.enterBackstage("13316957721")
            self.c.getCode()
            self.c.PayMoney()
        else:
            print("断言失败02")
        # !-----------------------------------------------------------------------------------------------! #

    # @data(*csvDataCode)
    # @unpack
    # #验证码登录的测试用例
    def test_CodeLoginFail(self, value_ID, value_Pwd,*args):
        self.b.jumopCodeLoginMod()
        self.b.codeIDLoginMod(value_ID)
        self.b.codePasswordLoginMod(value_Pwd)
        self.b.codeLoginBtn()
        #!-----------------------------------------------断言---------------------------------------------! #
        # self.eleText_01 = self.a.findElementTextSection("x", self.b.xpathHomePageId, 4)
        # self.eleText_02 = value_ID[len(value_ID) - 4:]
        # if self.eleText_01 == self.eleText_02:
        #     self.assertEqual(self.eleText_02,
        #                      self.eleText_01,
        #                      msg="登录的账号和右上角显示的不相同")
        #     self.b.safeEixt()
        if len(value_ID) < 11 or str.isdigit(value_ID) is False:
            print("提示的信息不对,01")
        elif len(value_Pwd) != 4 or str.isalnum(value_Pwd) is False:
            print("提示的信息不对,02")
        else:
            print("提示的信息不对,03")
            self.b.special()
        #!-----------------------------------------------------------------------------------------------! #

    def test_IDLoginSeccess(self):
        value_ID = "13316957721"
        value_Pwd = "z723113875"
        self.b.jumpIDLoginMod()
        self.b.iDLoginMod(value_ID)
        self.b.passwordLoginMod(value_Pwd)
        self.b.loginBtn()
        # !-----------------------------------------------断言---------------------------------------------! #
        self.eleText_01 = self.a.findElementTextSection("xpath", self.b.xpathHomePageId, 4)
        self.eleText_02 = value_ID[len(value_ID) - 4:]
        if self.eleText_01 == self.eleText_02:
            self.assertEqual(self.eleText_02,
                             self.eleText_01,
                             msg="登录的账号和右上角显示的不相同")
            self.b.safeEixt()
        else:
            print("断言失败")
        # !-----------------------------------------------------------------------------------------------! #

    # @data(*csvDataID)
    # @unpack
    # # 账号密码登录的测试用例
    def test_IDLoginFail(self, value_ID, value_Pwd, *arg):
        self.b.jumpIDLoginMod()
        self.b.iDLoginMod(value_ID)
        self.b.passwordLoginMod(value_Pwd)
        self.b.loginBtn()
        #!--------------------------------------------断言-----------------------------------------------! #
        # self.eleText_01 = self.a.findElementTextSection("x", self.b.xpathHomePageId, 4)
        # self.eleText_02 = value_ID[len(value_ID) - 4:]
        # if self.eleText_01 == self.eleText_02:
        #     self.assertEqual(self.eleText_02,
        #                      self.eleText_01,
        #                      msg="登录的账号和右上角显示的不相同")
        #     self.b.safeEixt()
        # else:
        if len(value_ID) == 0 or str.isdigit(value_ID) is False:
            self.assertEqual(
                self.a.findElementText("xpath", self.b.xpathPhoneNumFormatID),
                "请输入正确的手机号格式",
                msg="提示的信息不对")
        elif 11 > len(value_ID) > 0 or str.isdigit(value_ID) is False:
            self.assertEqual(
                self.a.findElementText("xpath", self.b.xpathPopUpTest),
                "请输入正确的手机号码",
                msg="提示的信息不对")
        elif len(value_Pwd) < 6 or len(value_Pwd) > 20 or str.isalnum(value_Pwd) is False:
            self.assertEqual(
                self.a.findElementText("xpath", self.b.xpathPwdLimit),
                "密码不能小于6位且不能大于20位",
                msg="提示的信息不对")
        else:
            self.assertEqual(
                self.a.findElementText("xpath", self.b.xpathPopUpTest),
                "账号或者密码错误" or "账号不存在",
                msg="提示的信息不对")
            self.b.special()
        #!----------------------------------------------------------------------------------------------! #

    # @classmethod
    def tearDownClass(self):
        self.a.quit()


#主函数入口
if __name__ == '__main__':
    from time import perf_counter
    import gevent

    start = perf_counter()
    run=MyTestCase()
    ll=(getCsvData(filepath=path1))
        # print (next(getCsvData(filepath=csvData1)) )
    # run.test_01(ll[1][0],ll[1][1])
    jobs=[]
    for value_ID,value_Pwd in ll:
        all_list=gevent.spawn(run.test_CodeLoginFail,value_ID,value_Pwd)
        jobs.append(all_list)
    gevent.joinall(jobs)
    # run.tearDownClass()
    pay_01=gevent.spawn(run.test_CodeLoginSeccess)
    pay_01.join()
    run.tearDownClass()
    end = perf_counter()
    print("**"*30+"\n","用时：{}".format(end - start), "*-*-" * 5)
