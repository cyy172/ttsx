from django.db import models


'''
用户模块
主要包括的功能有：
注册，使用register.html页面
登录，使用login.html页面
用户中心-个人信息：其中包括最近浏览的商品信息，这个功能需要等商品模块完成后再开发，使用info.html页面
用户中心-我的订单：显示当前登录用户的订单信息，需要完成订单模块后再开发，使用order.html页面
用户中心-收货地址，使用site.html页面
用户登录验证：如果用户未登录，则不能进入用户中心的相关页面，而是转到登录页面，如果登录成功则成功进入登记中心相关页面。
如果当前是登录状态则在顶部显示用户名和退出，如果当前是未登录状态，则提示登录、注册的链接。
'''


# 用户模块
class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    isDelect = models.BooleanField(default=False)  # 是否禁用：如果违规则禁用，而非物理删除
    # isValid=models.BooleanField(default=True)
    isActive=models.BooleanField(default=False)  # 是否激活：注册后需要发送邮件进行激活


# 定义地区模型类，存储省、市、区县信息
class AreaInfo(models.Model):
    atitle=models.CharField(max_length=30)  # 名称
    aParent=models.ForeignKey('self',null=True,blank=True)  # 关系


# 收件人收货地址
class AddressInfo(models.Model):
    sjr=models.CharField(max_length=20)  # 收件人
    sjh = models.CharField(max_length=11)  # 收件人电话
    addr=models.CharField(max_length=100)  # 收件地址
    isDelect = models.BooleanField(default=False)
    user=models.ForeignKey('UserInfo')  # 外键，与用户关联
    sheng = models.IntegerField()  # 省编号
    shi = models.IntegerField()  # 市编号
    qu = models.IntegerField()  # 区县编号

