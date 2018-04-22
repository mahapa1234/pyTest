# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from firstTest.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
            #request.session['user'] = username
            res = HttpResponseRedirect('/event_manage/')
            # 增加cookies
            res.set_cookie('user', username, 3600)
            return res
        else:
            return render(request, 'index.html', {'error':'username or password error!'})


#设置cookies及session
#装饰器，用于禁止打开未验证通过页面（设置页面必须验证）
# @login_required
# def event_manage(request):
#     # 获取cookies
#     # username = request.COOKIES.get('user', '')
#     # 获取session
#     username = request.session.get('user', '')
#     return render(request, 'event_manage.html', {'user':username})

#默认登录成功登录，显示发布会
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.COOKIES.get('user','')
    return render(request, "event_manage.html", {"user":username, "events":event_list})

#发布会搜索框
@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user":username, "events":event_list})

# @login_required
# def guest_manage(request):
#     username = request.session.get('user','')
#     guest_list = Guest.objects.all()
#     return render(request, "guest_manage.html",{"user":username, "guests":guest_list})

#用户组页面
@login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #如果page不是整数，取第一页面的数据
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user":username, "guests":contacts})

@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, "sign_index.html", {'event': event})

@login_required
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone','')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint':'phone error.'})
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event':event, 'hint':'event id or phone error.'})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint':'user has sign in.'})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'event':event, 'hint':'sign in success', 'guest':result})

@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response
