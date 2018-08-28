import urllib.request
import urllib
import json
import logging

logger = logging.getLogger('sms')


def send_sms(mobile, captcha):
    flag = True
    # 这个是短信API地址
    url = 'https://open.ucpaas.com/ol/sms/sendsms'

    # 准备一下头,声明body的格式
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    # 还有准备用Post传的值，这里值用字典的形式
    values = {
     "sid":"ccd4a5735819f7cafacdc028765f5f10",
     "token": '5c02f7fa050cc093f745649fc5554e64',
     "appid": "d356702b10614cb4ad6f5a15c4d58cd5",
     # "sid":"d356702b10614cb4ad6f5a15c4d58cd5",
     # "appid":"ccd4a5735819f7cafacdc028765f5f10",
     # "token":5c02f7fa050cc093f745649fc5554e64
     "templateid":"367136",
     "param":str(captcha),
     "mobile":mobile,
    }

    try:
        # 将字典格式化成bytes格式
        data = json.dumps(values).encode('utf-8')
        logger.info(f"即将发送短信: {data}")
        # 创建一个request,放入我们的地址、数据、头
        request = urllib.request.Request(url, data, headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        # html = '{"code":"000000","count":"1","create_date":"2018-07-23 13:34:06","mobile":"15811564298","msg":"OK","smsid":"852579cbb829c08c917f162b267efce6","uid":""}'
        code = json.loads(html)["code"]
        print(json.loads(html))
        print('code为'+code)
        if code == "000000":
            logger.info(f"短信发送成功：{html}")
            flag = True
        else:
            logger.info(f"短信发送失败：{html}")
            flag = False
    except Exception as ex:
        logger.info(f"出错了,错误原因：{ex}")
        flag = False
    return flag


if __name__ == "__main__":
    send_sms('15088993311', '6666')