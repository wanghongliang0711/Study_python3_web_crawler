"""
@author: wanghongliang
@file: 01_study_图形验证码的识别.py
@time: 2020/5/20 10:19 
"""
""" 正确率不高 不实用
知网注册页面
https://my.cnki.net/Register/CommonRegister.aspx
"""
import tesserocr
from PIL import Image

"""方法一"""
image = Image.open('CheckCode2.jpg')
resu = tesserocr.image_to_text(image)   # ns9Z
print(resu) # nsgZ  识别出错


"""方法二 没有方法一识别效果好"""
print(tesserocr.file_to_text("CheckCode2.jpg"))  # nsGZ


"""验证码处理 如转灰度、二值化等操作
Image 对象的 convert（）方法参数传人 L，即可将图片转化为灰度图像
传入 l 即可将图片进行二值化处理
我们还可以指定二值化的阔值。 上面的方法采用的是默认阔值 127。 
不过我们不能直接转化原因， 要将原图先转为灰度图像，然后再指定二值化阔值
"""
image = Image.open('CheckCode2.jpg')
image = image.convert("L")
threshold = 120  # 设置为 80 转化失败
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, "1")
image.show()
resu = tesserocr.image_to_text(image)   # ns9Z
print(resu) # nsgZ  识别出错

