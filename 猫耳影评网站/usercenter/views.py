from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
# Create your views here.


class Profile(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'uc_profile.html')
    def post(self,request):
        old_passwd = request.POST.get('oldpasswd')
        new_passwd1 = request.POST.get('newpasswd1')
        new_passwd2 = request.POST.get('newpasswd2')
        if new_passwd1 != new_passwd2:
            ret_info = {'code':'400','msg':'密码不一致'}
            return render(request, 'uc_profile.html', {'ret_info': ret_info})
        user = auth.authenticate(username=request.user.username,password=old_passwd)
        if user:
            user.set_password(new_passwd1)
            user.save()
            auth.logout(request)
            ret_info = {'code':'200','msg':'修改成功'}
        else:
            ret_info = {'code':'400','msg':'密码不正确'}
        return render(request,'uc_profile.html',{'ret_info':ret_info})


class Collect(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'uc_collect.html')


class Contribute(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'uc_contribute.html')

