from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import string
import re
import random
class Basic(object):
    def __init__(self):
        # !-----------------------------------------------无界面化---------------------------------------------! #
        self.arg = webdriver.FirefoxOptions()
        # # self.arg = webdriver.ChromeOptions()
        self.arg.add_argument('--headless')  # 无界面化.
        self.arg.add_argument('--disable-gpu')    # 配合上面的无界面化.不显示自动化控制的提示
        self.driver = webdriver.Firefox(options=self.arg)    #options=self.arg
        # # self.driver = webdriver.Chrome(options=self.arg)    #options=self.arg
        # !-----------------------------------------------打开浏览器-------------------------------------------! #
        # self.driver = webdriver.Ie()
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()

    def openWeb(self, URL):
        self.driver.maximize_window()
        self.driver.get(URL)
        self.Action = ActionChains(self.driver)

    #显示等待的传输值格式
    def pageWay(self, pagePath):
        value = (By.XPATH, pagePath)
        return value

    # 显示等待定位元素
    def findElement(self, value):
        element = WebDriverWait(self.driver, 50, 2).until(
            EC.presence_of_element_located(value)
        )
        return element

    # 定位页面元素文本
    def findElementText(self, value):
        pagePath = self.pageWay(value)
        element = self.findElement(pagePath)
        return element.text

    # 找到的文本元素切片操作
    def findElementTextSection(self, value, getLen):
        pagePath = self.pageWay(value)
        try:
            element = self.findElement(pagePath)
            textXpath = element.text
            return textXpath[len(textXpath) - getLen:]
        except:
            pass

    # 定位页面元素按钮
    def buttonClick(self, value):
        pagePath = self.pageWay(value)
        element = self.findElement(pagePath)
        element.click()

    # 获取列表标签下的所有子节点
    def getSonPoint(self, type, value):
        if type == "li":
            tempList = self.driver.find_element("xpath", value)
            strTemp = tempList.find_elements("tag name", "li")
            strLine = len(strTemp)
            return strLine
        elif type == "a":
            tempList = self.driver.find_element("xpath", value)
            strTemp = tempList.find_elements("tag name", "a")
            strLine = len(strTemp)
            return strLine

    # 定位页面元素输入
    def inputMessage(self, value_01, value_02):
        pagePath = self.pageWay(value_01)
        element = self.findElement(pagePath)
        element.send_keys(value_02)

    #随机
    def ran(self, firstNum, lastNum):
        return random.randint(firstNum, lastNum-1)

    # 弹窗处理
    def popUp(self, action):
        if action == "a":
            self.driver.switch_to.alert.accept()
        elif action == "d":
            self.driver.switch_to.alert.dismiss()
        else:
            pass

    # 鼠标事件（右键点击，鼠标悬停等）
    def mouseEvent(self, action, value):
        pagePath = self.pageWay(value)
        if action == "r":
            self.Action.context_click().perform()
        elif action == "m":
            element = self.Action.move_to_element(self.findElement(pagePath))
            return element.perform()
        else:
            pass

    # 下拉框选择
    def selectBox(self, value):
        pagePath = self.pageWay(value)
        opt = Select(self.findElement(pagePath))
        allOpt = opt.options
        strLen = len(allOpt)
        if strLen > 1:
            opt.select_by_index(random.randint(1, strLen-2))
        else:
            opt.select_by_index(0)

    # 取得标签页窗口句柄
    def WinHandle(self, num):
        winhandles = self.driver.window_handles[num]
        self.driver.switch_to.window(winhandles)

    #正则获取数据
    def regulGetData(self, type, path):
        if type == "num":
            return re.findall(r'\d+', path)
        else:
            pass

    # 到后台得到验证码
    def getCode(self, value):
        CodeMsg = self.findElementText(value)
        str_Code = self.regulGetData("num", CodeMsg)
        return str_Code[0]

    # 窗口下拉到底
    def winScroll(self):
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)

    # 随机数字或者号码
    def phoneNORandomGenerator(self, shape):
        if shape == "phone":
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "150", "151", "152",
                       "153", "155", "156", "157", "158", "159", "186", "187", "188"]
            return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        elif shape == "word":
            random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
            return random_str

    # 退出浏览器
    def quit(self):
        self.driver.quit()