import csv

path = r"D:\lovesgou\testcase\PagePath.CSV"

def getcsvData(filepath, key):
    dic = {}
    with(open(filepath, 'r', encoding='UTF-8')) as f:
        next(f)
        r = csv.reader(f)
        for i in r:
            dic[i[0]] = i[1]
    return dic[key]

class TestcaseElement(object):
        # ----------------------------------------登录模块----------------------------------------- #
        xpathHomePageLoginMod = getcsvData(path, "首页模块的登录按钮")    # 首页模块的登录按钮
        xpathCodeLoginMod = getcsvData(path, "登录模块的验证码登录")    # 登录模块的验证码登录
        xpathIdPwsLoginMod = getcsvData(path, "登录模块的账号密码登录")    # 登录模块的账号密码登录
        xpathEnterPhonenum = getcsvData(path, "验证码登录模块的输入手机号码")    # 验证码登录模块的输入手机号码
        xpathEnterCode = getcsvData(path, "验证码登录模块的输入验证码")    # 验证码登录模块的输入验证码
        xpathCodeLoginBtn = getcsvData(path, "验证码登录模块的登陆按钮")    # 验证码登录模块的登陆按钮
        xpathIdEnterPhonenum = getcsvData(path, "账号密码登录模块的输入手机号码")    # 账号密码登录模块的输入手机号码
        xpathIdEnterPws = getcsvData(path, "账号密码登录模块的输入密码")    # 账号密码登录模块的输入密码
        xpathIdEnterImg = getcsvData(path, "账号密码登录模块的验证码图片")    # 账号密码登录模块的验证码图片
        xpathIdEnterCode = getcsvData(path, "账号密码登录模块的输入验证码")    # 账号密码登录模块的输入验证码
        xpathIdPwsLoginBtn = getcsvData(path, "账号密码登录模块的登录按钮")    # 账号密码登录模块的登录按钮
        xpathHomePageId = getcsvData(path, "首页右上角的账号名称")    # 首页右上角的账号名称
        xpathSafeExit = getcsvData(path, "安全退出按钮")    # 安全退出按钮
        xpathPopUpBtn = getcsvData(path, "登录模块登录弹窗的确定按钮")    # 登录模块登录弹窗的确定按钮
        xpathPopUpTest = getcsvData(path, "登录模块登录弹窗中的内容")    # 登录模块登录弹窗中的内容
        xpathPhoneNumFormat = getcsvData(path, "请输入正确的手机号格验证码登录")    # 请输入正确的手机号格式(验证码登录)
        xpathPhoneNumFormatID = getcsvData(path, "请输入正确的手机号格账号密码登录")    # 请输入正确的手机号格式(账号密码登录)
        xpathCodeFormat = getcsvData(path, "请输入正确的验证码格式")    # 请输入正确的验证码格式
        xpathPwdLimit = getcsvData(path, "密码不能小于6位且不能大于20位")    # 密码不能小于6位且不能大于20位

        # ----------------------------------------支付流程----------------------------------------- #
        xpathHomePageBtn = getcsvData(path, "登录之后的首页按钮")    # 登录之后的首页按钮
        xpathAllWares = getcsvData(path, "全部商品分类")    #全部商品分类
        xpathHomeOddsBtn = getcsvData(path, "首页的特惠产品按钮")    # 首页的特惠产品按钮
        # xpathTopSortList = getcsvData(path, "商品分类一级列表")    # 商品分类一级列表
        # xpathSecondSortList = getcsvData(path, "商品分类二级列表")  # 商品分类二级列表
        # xpathThirdSortList = getcsvData(path, "商品分类三级列表")  # 商品分类三级列表
        xpathTopSort = getcsvData(path, "商品分类一级")    # 商品分类一级
        xpathSecondSort = getcsvData(path, "商品分类二级")    # 商品分类二级
        xpathThirdSort = getcsvData(path, "商品分类三级")    # 商品分类三级
        xpathWaresMag = getcsvData(path, "产品翻页信息")    # 产品翻页信息
        xpathWaresBtn = getcsvData(path, "点击产品")    # 点击产品
        xpathWaresName = getcsvData(path, "产品名称")    # 产品名称
        xpathNomsBtn = getcsvData(path, "点击规格")    # 点击规格
        xpathShopCarBtn = getcsvData(path, "加入购物车按钮")    # 加入购物车按钮
        xpathBuyNowBtn = getcsvData(path, "立即购买按钮")    # 立即购买按钮
        xpathJoinCarImg = getcsvData(path, "加入购物车图标")    # 加入购物车图标
        xpathCheckWareMag = getcsvData(path, "查看商品详情按钮")    # 查看商品详情按钮
        xpathGoCarWareMag = getcsvData(path, "购物车中查看商品详情")    # 购物车中查看商品详情
        xpathGoShopCarPay = getcsvData(path, "去购物车结算按钮")    # 去购物车结算按钮
        xpathAllCheck = getcsvData(path, "全选框")    # 全选框
        xpathGoPay = getcsvData(path, "去结算按钮")    # 去结算按钮
        xpathConsigneeMag = getcsvData(path, "收货人信息默认文本")    # 收货人信息默认文本(暂无收货地址~)
        xpathAddConsignee = getcsvData(path, "新增收获人地址")    # 新增收获人地址
        xpathConsignee = getcsvData(path, "收货人")    # 收货人
        xpathPhoneNum = getcsvData(path, "手机号")    # 手机号
        xpathAddr_Province = getcsvData(path, "收货地址省")    # 收货地址(省)
        xpathAddr_City = getcsvData(path, "收货地址市")  # 收货地址(市)
        xpathAddr_Area = getcsvData(path, "收货地址区")  # 收货地址(区)
        xpathDetailAddr = getcsvData(path, "详细地址")    # 详细地址
        xpathDetailHelp = getcsvData(path, "详细地址提示信息")    # 详细地址提示信息(请填写详细地址)
        xpathCheckBox = getcsvData(path, "检查框")    # 检查框(设为默认地址)
        xpathWaresValue = getcsvData(path, "商品的总价格")    # 商品的总价格
        xpathFare = getcsvData(path, "运费")    # 运费
        xpathAllValue = getcsvData(path, "应付的总金额")    # 应付的总金额
        xpathPlaceOrder = getcsvData(path, "提交订单")    # 提交订单
        xpathTips = getcsvData(path, "弹窗的提示信息")    # 弹窗的提示信息(请选择收货地址)
        xpathCPMBtn = getcsvData(path, "弹窗的按钮")    # 弹窗的按钮
        xpathSaveBtn = getcsvData(path, "保存按钮")    # 保存按钮
        xpathChooseAddr = getcsvData(path, "选择一个地址")    # 选择一个地址
        xpathBalancePay = getcsvData(path, "选择支付方式(余额支付)")    # 选择支付方式(余额支付)
        xpathInputCode = getcsvData(path, "输入4位数短信验证码")    # 输入4位数短信验证码
        xpathSendCode = getcsvData(path, "发送验证码")    # 发送验证码
        xpathPayBtn = getcsvData(path, "立即支付按钮")    # 立即支付按钮
        xpathAddrDel = getcsvData(path, "删除收货人地址按钮")    # 删除收货人地址按钮
        xpathSetDefAddr = getcsvData(path, "设为默认地址按钮")    # 设为默认地址按钮
        xpathPopAccBtn = getcsvData(path, "弹窗的确定按钮")    # 弹窗的确定按钮
        xpathPopCanBtn = getcsvData(path, "弹窗的取消按钮")    # 弹窗的取消按钮
        xpathMoreAddrBtn = getcsvData(path, "更多地址按钮")    # 更多地址按钮
        xpathAddrList = getcsvData(path, "地址的列表")    # 地址的列表
        xpathConsigneeMagCheck = getcsvData(path, "收货人信息选中框")    # 收货人信息选中框

        # ----------------------------------------后台管理----------------------------------------- #
        xpathBackstageUser = getcsvData(path, "用户名")    # 用户名
        xpathBackstagePwd = getcsvData(path, "密码")    # 密码
        xpathBackstageCode = getcsvData(path, "验证码")    # 验证码
        xpathLoginBtn = getcsvData(path, "登陆按钮")    # 登陆按钮
        xpathSysBtn = getcsvData(path, "系统按钮")    # 系统按钮
        xpathSysDaily = getcsvData(path, "系统日志按钮")    # 系统日志按钮
        xpathNoteDaily = getcsvData(path, "短信日志按钮")    # 短信日志按钮
        xpathNoteMsg = getcsvData(path, "短信内容")    # 短信内容
        xpathUserBtn = getcsvData(path, "用户按钮")    # 用户按钮
        xpathExitBtn = getcsvData(path, "退出按钮")    # 退出按钮