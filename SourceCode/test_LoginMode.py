from tools.test_basic import Basic
from tools.test_testcasepagelement import TestcaseElement


class Login(TestcaseElement):
    def __init__(self, driver:Basic):
        self.dr = driver

    #跳转到登录模块(验证码登录)
    def jumopCodeLoginMod(self):
        self.dr.buttonClick(self.xpathHomePageLoginMod)
        self.dr.buttonClick(self.xpathCodeLoginMod)

    #跳转到登录模块(账号密码登录)
    def jumpIDLoginMod(self):
        self.dr.buttonClick(self.xpathHomePageLoginMod)
        self.dr.buttonClick(self.xpathIdPwsLoginMod)

    #验证码登录的账号
    def codeIDLoginMod(self, value):
        self.dr.inputMessage(self.xpathEnterPhonenum, value)

    #验证码登录的验证码
    def codePasswordLoginMod(self, value):
        self.dr.inputMessage(self.xpathEnterCode, value)

    #账号密码登录的账号
    def iDLoginMod(self, value):
        self.dr.inputMessage(self.xpathIdEnterPhonenum, value)

    #账号密码登录的密码
    def passwordLoginMod(self, value):
        self.dr.inputMessage(self.xpathIdEnterPws, value)

    #登录按钮的点击(验证码模块)
    def codeLoginBtn(self):
        self.dr.buttonClick(self.xpathCodeLoginBtn)

    #登录按钮的点击(账号登录模块模块)
    def loginBtn(self):
        self.dr.buttonClick(self.xpathIdPwsLoginBtn)

    #安全退出
    def safeEixt(self):
        self.dr.mouseEvent("m", self.xpathHomePageId)
        self.dr.mouseEvent("m", self.xpathSafeExit)
        self.dr.buttonClick(self.xpathSafeExit)

    # 弹窗的确认按钮
    def special(self):
        self.dr.buttonClick(self.xpathPopUpBtn)