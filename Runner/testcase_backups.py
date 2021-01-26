import time

from SourceCode.test_LoginMode import Login
from SourceCode.test_PaymentProcessMode import PayMode
from tools.test_basic import Basic
from ddt import ddt, data, unpack

import pytest
import unittest
import csv

def getCsvData(filepath):
    f = open(filepath, encoding='UTF-8')
    next(f)
    r = csv.reader(f)
    return list(r)

csvDataCode = getCsvData(r"D:\lovesgou\testcase\CodeTest.CSV")
csvDataID = getCsvData(r"D:\lovesgou\testcase\IDPasswordTest.CSV")
csvCodeLoginSuccess = getCsvData(r"D:\lovesgou\testcase\CodeLoginSuccess.CSV")
csvIDLoginSuccess = getCsvData(r"D:\lovesgou\testcase\IDLoginSuccess.CSV")
# path = r"D:\lovesgou\LoginMod\testcase\PagePath.CSV"

@ddt
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = Basic()    # 基本工具类的实例化对象
        cls.b = Login(cls.a)    # 登录页面操作的实例化对象
        cls.c = PayMode(cls.a)    # 支付流程模块的实例化对象
        cls.a.openWeb("http://demo.lovesgou.com/")
        cls.a.driver.implicitly_wait(5)

    @data(*csvCodeLoginSuccess)
    @unpack
    def test_01_PayProcess(self, value_ID, value_Pwd):
        self.b.jumopCodeLoginMod()
        self.b.codeIDLoginMod(value_ID)
        self.b.codePasswordLoginMod(value_Pwd)
        self.b.codeLoginBtn()
        # !-----------------------------------------------断言---------------------------------------------! #
        self.eleText_01 = self.a.findElementTextSection("xpath", self.b.xpathHomePageId, 4)
        self.eleText_02 = value_ID[len(value_ID) - 4:]
        if self.eleText_01 == self.eleText_02:
            self.assertEqual(self.eleText_02,
                             self.eleText_01,
                             msg="登录的账号和右上角显示的不相同")
            self.c.chooseWares()
            self.c.clickWare()
            self.c.joinShopCar()
            self.c.goShopCarSett()
            self.c.allCheckBox()
            self.c.goSett()
            self.c.addConsigneeAddr(self.a.phoneNORandomGenerator("word"),
                                    self.a.phoneNORandomGenerator("phone"),
                                    self.a.phoneNORandomGenerator("word"))
            self.c.windowScrrollBy()
            self.c.placeOrder()
            self.c.balancePaySendCode()
            self.c.backstage()
            self.c.enterBackstage("13316957721")
            self.c.getCode()
            self.c.PayMoney()
            self.b.safeEixt()
        else:
            print("断言失败")
        # !-----------------------------------------------------------------------------------------------! #

    @data(*csvDataCode)
    @unpack
    #验证码登录的测试用例
    def test_02_CodeLoginFail(self, value_ID, value_Pwd,*args):
        self.b.jumopCodeLoginMod()
        self.b.codeIDLoginMod(value_ID)
        self.b.codePasswordLoginMod(value_Pwd)
        self.b.codeLoginBtn()
        #!-----------------------------------------------断言---------------------------------------------! #
        if len(value_ID) < 11 or str.isdigit(value_ID) is False:
            self.assertEqual(self.a.findElementText("xpath", self.b.xpathPhoneNumFormat),
                             "请输入正确的手机号格式",
                             msg="提示的信息不对")
        elif len(value_Pwd) != 4 or str.isalnum(value_Pwd) is False:
            self.assertEqual(self.a.findElementText("xpath", self.b.xpathCodeFormat),
                             "请输入正确的验证码格式",
                             msg="提示的信息不对")
        else:
            self.assertEqual(self.a.findElementText("xpath", self.b.xpathPopUpTest),
                             "内部验证码不正确",
                             msg="提示的信息不对")
            self.b.special()
        #!-----------------------------------------------------------------------------------------------! #

    @data(*csvIDLoginSuccess)
    @unpack
    def test_03_IDLoginSeccess(self, value_ID, value_Pwd):
        self.a.openWeb("http://demo.lovesgou.com")
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

    @data(*csvDataID)
    @unpack
    # 账号密码登录的测试用例
    def test_04_IDLoginFail(self, value_ID, value_Pwd, *arg):
        self.b.jumpIDLoginMod()
        self.b.iDLoginMod(value_ID)
        self.b.passwordLoginMod(value_Pwd)
        self.b.loginBtn()
        #!--------------------------------------------断言-----------------------------------------------! #
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

    @classmethod
    def tearDownClass(cls):
        cls.a.quit()

if __name__=="__main__":
    unittest.main()