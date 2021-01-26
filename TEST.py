import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

arg = webdriver.FirefoxOptions()
# arg = webdriver.IeOptions()
arg.add_argument('--headless')  # 无界面化.
arg.add_argument('--disable-gpu')    # 配合上面的无界面化.不显示自动化控制的提示
dr = webdriver.Firefox(options=arg)
# dr = webdriver.Ie(options=arg)
dr.get("http://demo.lovesgou.com/tags-tehui.html?cateid1=0&cateid2=0&cateid3=0&sortby=update_time&orderby=desc")

path_01 = "/html/body/div[3]/div/div/div[1]/div/div/div[1]/div[1]/ul"
path_02 = "/html/body/div[3]/div/div/div[1]/div/div/div[2]/div[1]/ul"

path_03 = "/html/body/div[3]/div/div/div[1]/div/div/div[1]/div[1]/ul/a[{}]"
path_04 = "/html/body/div[3]/div/div/div[1]/div/div/div[2]/div[1]/ul/a[{}]"

aa = dr.find_element("xpath", path_01)
bb = aa.find_elements("tag name", "a")
aa.click()

aa_01 = dr.find_element("xpath", path_02)
bb_01 = aa.find_elements("tag name", "a")

str_len = len(bb)

cc = dr.find_element("xpath", path_03.format(random.randint(1, str_len-1))).text
print(cc)

cc_01 = dr.find_element("xpath", path_04.format(random.randint(1, str_len-1))).text
print(cc_01)