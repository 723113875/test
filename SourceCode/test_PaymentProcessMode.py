import random
import time

from tools.test_basic import Basic
from tools.test_testcasepagelement import TestcaseElement

class PayMode(TestcaseElement):
    def __init__(self, driver:Basic):
        self.dr = driver
        self.ranXpath = 0

    # 首页模块的全部商品分类(随机点击)
    def allWares(self):
        self.dr.buttonClick(self.xpathHomePageBtn)
        ranNum = random.randint(1, 7)
        self.dr.buttonClick(self.xpathAllWares.format(ranNum))

    # 首页模块的按钮点击(特惠产品)
    def chooseWares(self):
        self.dr.buttonClick(self.xpathHomeOddsBtn)

    # 商品分类点击(一级二级三级分类)
    def waresSort(self):
        self.dr.buttonClick(self.xpathTopSort)
        self.dr.buttonClick(self.xpathSecondSort)
        self.dr.buttonClick(self.xpathThirdSort)

    # 随机点击
    def clickWare(self, path, firstNum, num):
        strNum = self.dr.regulGetData("num", self.dr.findElementText(path))
        sumNum = int(strNum[num]) - int(strNum[num - 1])
        self.ranXpath = self.dr.ran(firstNum, sumNum)
        self.dr.buttonClick(self.xpathWaresBtn.format(self.ranXpath))
        self.dr.WinHandle(1)

    # 点击加入购物车
    def joinShopCar(self):
        self.dr.buttonClick(self.xpathShopCarBtn)

    # 点击立即购买
    def buyNowBtn(self):
        self.dr.buttonClick(self.xpathBuyNowBtn)

    # 加入购物车图标
    def joinCarImg(self):
        self.dr.buttonClick(self.xpathJoinCarImg)

    # 点击查看商品详情
    def checkWaresMag(self):
        self.dr.buttonClick(self.xpathCheckWareMag)

    # 去购物车结算
    def goShopCarSett(self):
        self.dr.buttonClick(self.xpathGoShopCarPay)

    # 购物车中查看商品详情
    def goShopCarWaresMag(self):
        self.dr.buttonClick(self.xpathGoCarWareMag)

    # 点击全选
    def allCheckBox(self):
        self.dr.buttonClick(self.xpathAllCheck)

    # 点击去结算
    def goSett(self):
        self.dr.buttonClick(self.xpathGoPay)

    # 更多地址按钮和随机选择一条地址
    def ranChoseAddr(self):
        self.dr.buttonClick(self.xpathMoreAddrBtn)
        strLine = self.dr.getSonPoint("li", self.xpathAddrList)
        self.dr.buttonClick(self.xpathConsigneeMagCheck.format(self.dr.ran(1, strLine)))

    # 新增收货人地址
    def addConsigneeAddr(self, valueName, valuePhone, valueDetail):
        self.dr.buttonClick(self.xpathAddConsignee)
        self.dr.inputMessage(self.xpathConsignee, valueName)
        self.dr.inputMessage(self.xpathPhoneNum, valuePhone)
        self.dr.selectBox(self.xpathAddr_Province)
        self.dr.selectBox(self.xpathAddr_City)
        self.dr.selectBox(self.xpathAddr_Area)
        self.dr.inputMessage(self.xpathDetailAddr, valueDetail)
        self.dr.buttonClick(self.xpathCheckBox)
        self.dr.buttonClick(self.xpathSaveBtn)
        time.sleep(3)

    # 删除收货人地址
    def delConsigneeAddr(self):
        self.dr.buttonClick(self.xpathAddrDel)
        self.dr.buttonClick(self.xpathPopCanBtn)
        self.dr.driver.refresh()
        self.dr.buttonClick(self.xpathAddrDel)
        self.dr.buttonClick(self.xpathPopAccBtn)

    # 设为默认地址
    def setDefAddr(self):
        self.dr.driver.refresh()
        # self.dr.findElement(self.xpathAddrList)
        self.dr.buttonClick(self.xpathSetDefAddr)
        self.dr.buttonClick(self.xpathPopCanBtn)
        self.dr.driver.refresh()
        self.dr.buttonClick(self.xpathSetDefAddr)
        self.dr.buttonClick(self.xpathPopAccBtn)

    #滚动条下拉
    def windowScrrollBy(self):
        self.dr.winScroll()

    # 提交订单按钮
    def placeOrder(self):
        self.dr.driver.refresh()
        self.dr.buttonClick(self.xpathPlaceOrder)

    # 余额支付发送送验证码
    def balancePaySendCode(self):
        self.dr.buttonClick(self.xpathBalancePay)
        while(True):
            if self.dr.findElementText(self.xpathSendCode) == "发送验证码":
                self.dr.buttonClick(self.xpathSendCode)
                break
            else:
                pass

    # 打开后台管理系统
    def backstage(self):
        self.dr.WinHandle(0)
        self.dr.openWeb("http://demo.admin.lovesgou.com/")

    #进入后台系统
    def enterBackstage(self, value, password):
        self.dr.inputMessage(self.xpathBackstageUser, value)
        self.dr.inputMessage(self.xpathBackstagePwd, password)
        self.dr.inputMessage(self.xpathBackstageCode, "8888")
        self.dr.buttonClick(self.xpathLoginBtn)
        self.dr.buttonClick(self.xpathSysBtn)
        self.dr.buttonClick(self.xpathSysDaily)
        self.dr.buttonClick(self.xpathNoteDaily)

    # 退出后台
    def exitBackstage(self):
        self.dr.buttonClick(self.xpathUserBtn)
        self.dr.buttonClick(self.xpathExitBtn)

    # 获取短信验证码
    def getCode(self):
        self.dr.driver.switch_to.frame("RightFrameBox")
        value = self.dr.getCode(self.xpathNoteMsg)
        self.dr.WinHandle(1)
        self.dr.inputMessage(self.xpathInputCode, value)
        self.dr.WinHandle(0)
        self.exitBackstage()
        self.dr.driver.close()

    #立即支付按钮
    def PayMoney(self):
        self.dr.WinHandle(0)
        self.dr.buttonClick(self.xpathPayBtn)