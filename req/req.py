import requests
url="http://demo.merchant.lovesgou.com"
url= url+"/work_order/upload.html"
img_path=r"C:\Users\Administrator\Desktop\ysk\BUG\BUG列表清单.xlsx"
img_name="BUG列表清单.xlsx"
img_type='image/jpeg'
with open(img_path , "rb")as f_abs:
    body = {
        # 'asyupload': (img_name, f_abs, img_type)
        "upfile" : (img_name, f_abs, img_type)
        # 图片的名称、图片的绝对路径、图片的类型（就是后缀）
    }

head={
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"X-Requested-With": "XMLHttpRequest",
"Cookie": "PHPSESSID=8dec6a989b90961f6b8e6414b048e523"
}
print(url,body)
kk= requests.post(url=url,headers=head,files=body)
print(kk.text)