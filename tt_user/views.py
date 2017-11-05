from django.shortcuts import render
from .models import *
from hashlib import sha1
from django.http import HttpResponse


# 用户注册
def register(request):
    context = {}
    return render(request, 'tt_user/register.html', context)


# 用户注册后处理保存数据
def register_handle(request):
    # 接收数据
    dict = request.POST
    uname = dict.get('user_name')
    pwd = dict.get('pwd')
    email = dict.get('email')
    # 加密
    s1 = sha1()
    s1.update(pwd.encode('utf-8'))
    pwd_sha1 = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = pwd_sha1
    user.email = email
    user.save()
    # 提示激活
    return HttpResponse('请到邮箱激活，再进行登录')