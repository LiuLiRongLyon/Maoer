from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from django.views.generic import View
from moviesapp.models import UserInfo
from django.core.cache import cache
from django.contrib.auth import logout as auth_logout,login as auth_login
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import auth
import logging
logger = logging.getLogger('accounts')


class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect(reverse('master'))
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('passwd','')
        captcha = request.POST.get('captcha','')
        session_captcha = request.session.get('captcha_code','')
        if captcha.lower() == session_captcha.lower():
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                logger.debug(f'用户{user}登录成功')
                return redirect(reverse('master'))
            else:
                logger.debug(f'用户{username}不存在')
                return render(request, 'login.html')
        else:
            logger.debug('验证码错误')
            return render(request, 'login.html')


class Registe(View):
    def get(self,request):
        return render(request,'registe.html')
    def post(self,request):
        ret = {"status": 400, "msg": "调用方式错误"}
        username =request.POST.get('username')
        tel =request.POST.get('tel')
        passwd =request.POST.get('passwd')
        test =request.POST.get('test')
        cache_test = cache.get(tel)
        if test == cache_test:
            user = UserInfo.objects.create(username=username,tel=tel,password=make_password(passwd))
            user.save()
            logger.debug(f'新用户{user}注册成功')
            ret['status'] = 200
            ret['msg'] = "注册成功"
            return JsonResponse(ret)
        logger.debug(f'新用户{username}注册失败')
        return JsonResponse(ret)


def logout(request):
    logger.debug(f'{request.user}退出系统')
    auth_logout(request)
    return redirect(reverse('accounts:login'))