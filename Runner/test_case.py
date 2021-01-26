# import sys
# sys.path.append("D:\lovesgou")
from SourceCode.test_LoginMode import Login
from SourceCode.test_PaymentProcessMode import PayMode
from tools.test_basic import Basic

import pytest
import csv

def getCsvData(filepath):
    f = open(filepath, encoding='UTF-8')
    next(f)
    r = csv.reader(f)
    return list(r)

str_URL = "http://demo.lovesgou.com/"
csvDataCode = getCsvData(r"D:\lovesgou\testcase\CodeTest.CSV")
csvDataID = getCsvData(r"D:\lovesgou\testcase\IDPasswordTest.CSV")
csvCodeLoginSuccess = getCsvData(r"D:\lovesgou\testcase\CodeLoginSuccess.CSV")
csvIDLoginSuccess = getCsvData(r"D:\lovesgou\testcase\IDLoginSuccess.CSV")

class Test_Class():

    def setup_class(self):
        self.a = Basic()    # 基本工具类的实例化对象
        self.b = Login(self.a)    # 登录页面操作的实例化对象
        self.c = PayMode(self.a)    # 支付流程模块的实例化对象
        self.a.openWeb(str_URL)

    # 支付流程(加入购物车支付)和验证码登录成功的测试用例
    @pytest.mark.parametrize("value_ID, value_pwd", csvCodeLoginSuccess)
    def test_01_CodePayProcess(self, value_ID,value_pwd):
        self.b.jumopCodeLoginMod()
        self.b.codeIDLoginMod(value_ID)
        self.b.codePasswordLoginMod(value_pwd)
        self.b.codeLoginBtn()
        # !-----------------------------------------------用户名断言----------------------------------------------! #
        self.eleText_01 = self.a.findElementTextSection(self.b.xpathHomePageId, 4)
        self.eleText_02 = value_ID[len(value_ID) - 4:]
        assert self.eleText_01 == self.eleText_02
        self.c.allWares()
        self.c.chooseWares()
        # self.c.waresSort()
        self.c.windowScrrollBy()
        self.c.clickWare(self.b.xpathWaresMag, 1, 2)
        self.c.joinShopCar()
        self.c.goShopCarSett()
        self.c.joinCarImg()
        self.c.allCheckBox()
        self.c.goSett()
        self.c.addConsigneeAddr(self.a.phoneNORandomGenerator("word"),
                                self.a.phoneNORandomGenerator("phone"),
                                self.a.phoneNORandomGenerator("word"))
        self.c.ranChoseAddr()
        self.c.delConsigneeAddr()
        self.c.setDefAddr()
        self.c.windowScrrollBy()
        self.c.placeOrder()
        self.c.balancePaySendCode()
        self.c.backstage()
        self.c.enterBackstage("13316957721", "111111")
        self.c.getCode()
        self.c.PayMoney()
        self.b.safeEixt()
        # !-----------------------------------------------------------------------------------------------! #

    # 账号密码登录失败的测试用例
    @pytest.mark.parametrize("value_ID, value_pwd", csvDataID)
    def test_02_IDLoginFail(self, value_ID, value_pwd):
        self.b.jumpIDLoginMod()
        self.b.iDLoginMod(value_ID)
        self.b.passwordLoginMod(value_pwd)
        self.b.loginBtn()
        #!--------------------------------------------断言-----------------------------------------------! #
        if len(value_ID) == 0 or str.isdigit(value_ID) is False:
            assert self.a.findElementText(self.b.xpathPhoneNumFormatID) == "请输入正确的手机号格式"
        elif 11 > len(value_ID) > 0 or str.isdigit(value_ID) is False:
            assert self.a.findElementText(self.b.xpathPopUpTest) == "请输入正确的手机号码"
        elif len(value_pwd) < 6 or len(value_pwd) > 20 or\
                str.isalnum(value_pwd) is False:
            assert self.a.findElementText(self.b.xpathPwdLimit) == "密码不能小于6位且不能大于20位"
        else:
            assert self.a.findElementText(self.b.xpathPopUpTest) == "账号或者密码错误" or "账号不存在"
            self.b.special()
        #!----------------------------------------------------------------------------------------------! #

    #验证码登录失败的测试用例
    @pytest.mark.parametrize("value_ID, value_pwd", csvDataCode)
    def test_03_CodeLoginFail(self, value_ID, value_pwd):
        self.b.jumopCodeLoginMod()
        self.b.codeIDLoginMod(value_ID)
        self.b.codePasswordLoginMod(value_pwd)
        self.b.codeLoginBtn()
        #!-----------------------------------------------断言---------------------------------------------! #
        if len(value_ID) < 11 or str.isdigit(value_ID) is False:
            assert self.a.findElementText(self.b.xpathPhoneNumFormat) == "请输入正确的手机号格式"
        elif len(value_pwd) != 4 or str.isalnum(value_pwd) is False:
            assert self.a.findElementText(self.b.xpathCodeFormat) == "请输入正确的验证码格式"
        else:
            assert self.a.findElementText(self.b.xpathPopUpTest) =="内部验证码不正确"
            self.b.special()
        #!-----------------------------------------------------------------------------------------------! #

    # 支付流程(立即购买)和账号密码登录
    @pytest.mark.parametrize("value_ID, value_pwd", csvIDLoginSuccess)
    def test_05_IDPayProcess(self, value_ID, value_pwd):
        self.b.jumpIDLoginMod()
        self.b.iDLoginMod(value_ID)
        self.b.passwordLoginMod(value_pwd)
        self.b.loginBtn()
        # !-----------------------------------------------用户名断言----------------------------------------------! #
        self.eleText_01 = self.a.findElementTextSection(self.b.xpathHomePageId, 4)
        self.eleText_02 = value_ID[len(value_ID) - 4:]
        assert self.eleText_02 == self.eleText_01
        self.c.chooseWares()
        self.c.windowScrrollBy()
        self.c.clickWare(self.b.xpathWaresMag, 1, 2)
        self.c.buyNowBtn()
        self.c.placeOrder()
        self.c.balancePaySendCode()
        self.c.backstage()
        self.c.enterBackstage("13316957721", "111111")
        self.c.getCode()
        self.c.PayMoney()
        self.b.safeEixt()
        # !-----------------------------------------------------------------------------------------------! #

    def teardown_class(self):
        self.a.quit()

if __name__ == "__main__":
    pytest.main([__file__, "--reruns","2"])