from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^get_captcha/$', views.get_captcha,name='get_captcha'),
    url(r'^get_mobile_captcha/$', views.get_mobile_captcha, name='get_mobile_captcha'),
    url(r'^check_username/$', views.check_username, name='check_username'),
]