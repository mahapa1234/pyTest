# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # return HttpResponse("hello world")
    return render(request, "index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # if username == 'admin' and password == 'admin123':
        user = auth.authenticate(username=username, password=password)
        # 如认证不通过，user返回为空
        if user is not None:
            auth.login(request, user)
            # 增加session
            request.session['user'] = username
            res = HttpResponseRedirect('/event_manage/')
            # 增加cookies
            # res.set_cookie('user', username, 3600)
            return res
        else:
            return render(request, 'index.html', {'error':'username or password error!'})


#装饰器，用于禁止打开未验证通过页面（设置页面必须验证）
@login_required
def event_manage(request):
    # 获取cookies
    # username = request.COOKIES.get('user', '')
    # 获取session
    username = request.session.get('user', '')
    return render(request, 'event_manage.html', {'user':username})

