# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django import forms
from django.contrib import auth
from models import BusinessClass, User
from django.contrib.auth import authenticate,login as auth_login ,logout
from django.conf import settings
from django.utils.importlib import import_module

def bclist(request):
    BusinessClasslist = BusinessClass.objects.all()
    return render(request, 'liguang_first/bc_list_view.html',
                  {'BusinessClasslist': BusinessClasslist})


def rendertoHome(request):
    # user baidu as homePage
    return HttpResponseRedirect("http://www.baidu.com/")

# 表单


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# 注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            User.objects.create(username=username, password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',
                              {'uf': uf}, context_instance=RequestContext(req))

# 登陆


def alogin(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = auth.authenticate(username=username, password=password)
            # if user:
            # 比较成功，跳转index
            #     response = HttpResponseRedirect('/liguang_first/index/')
            # 将username写入浏览器cookie,失效时间为3600
            #     response.set_cookie('username', username, 3600)
            #     return response
            # else:
            # 比较失败，还在login
            #     return HttpResponseRedirect('/liguang_first/login/')

            if user is not None:
                if user.is_active:
                    auth_login(req, user)
                    print req.user
                    response = HttpResponseRedirect('/liguang_first/index/')
                    response.set_cookie('username', username, 3600)
                    return response
                else:
                    return HttpResponseRedirect('/liguang_first/login/')

    else:
        uf = UserForm()
    return render_to_response('login.html',
                              {'uf': uf}, context_instance=RequestContext(req))

# 登陆成功


def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username': username})

# 退出


def logout(req):
    response = HttpResponse('logout !!')
    # 清理cookie里保存username
    response.delete_cookie('username')
    return response


def register2(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('Please Enter account')
        else:
            account = request.POST.get('account')
        if not request.POST.get('password'):
            errors.append('Please Enter password')
        else:
            password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('Please Enter password2')
        else:
            password2 = request.POST.get('password2')
        if not request.POST.get('email'):
            errors.append('Please Enter email')
        else:
            email = request.POST.get('email')

        if password is not None and password2 is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('password2 is diff password ')

        if account is not None and password is not None and password2 is not None and email is not None and CompareFlag:
            user = User.objects.create_user(account, email, password)
            user.is_active = True
            user.save
            return HttpResponseRedirect('/liguang_first/login')

    return render_to_response('liguang_first/register2.html', {'errors': errors})


def alogout(request):
    logout(request)
    return HttpResponseRedirect('liguang_first/index')
