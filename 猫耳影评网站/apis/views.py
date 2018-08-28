from django.shortcuts import HttpResponse
from django.http import JsonResponse
from io import BytesIO
from libs import patcha,sms
import random
import base64
import logging
logger = logging.getLogger('apis')


def get_captcha(request):
    f = BytesIO() # 直接在内存开辟一点空间存放临时生成的图片
    img,code = patcha.create_validate_code()  # 调用check_code生成照片和验证码
    request.session['captcha_code'] = code  # 将验证码存在服务器的session中，用于校验
    print('后端验证码是',request.session.get('captcha_code'))
    img.save(f,'PNG')  # 生成的图片放置于开辟的内存中
    # 将内存的数据读取出来，并以HttpResponse返回
    ret_type = 'data:image/jpg;base64,'.encode()
    ret = ret_type+base64.encodebytes(f.getvalue())
    del f
    return HttpResponse(ret)


from django.core.cache import cache
def get_mobile_captcha(request):
    ret = {"code": 200, "msg": "验证码发送成功！"}
    try:
        mobile = request.GET.get("mobile")
        if mobile is None: raise ValueError("手机号不能为空！")
        mobile_captcha = "".join(random.choices('0123456789', k=6))
        cache.set(mobile, mobile_captcha, 300)  # 将短信验证码写入redis
        mobile_captcha_reids = cache.get(mobile)
        print(mobile_captcha_reids)
        if not sms.send_sms(mobile, mobile_captcha):
            raise ValueError('发送短信失败')
    except Exception as ex:
        logger.error(ex)
        ret = {"code": 400, "msg": "短信发送失败！"}
    return JsonResponse(ret)


from moviesapp.models import UserInfo
def check_username(request):
    user = request.GET.get('username','')
    if UserInfo.objects.filter(username=user):
        ret = {'msg':'重名了'}
    else:
        ret = {'msg':'正确'}
    print(ret)
    return JsonResponse(ret)