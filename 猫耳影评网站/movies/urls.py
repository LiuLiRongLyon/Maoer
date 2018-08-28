"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from moviesapp import views
from django.views.static import serve
from .settings import MEIDA_ROOT
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts'), name='accounts'),  # 登录与注册
    url(r'^usercenter/',include('usercenter.urls',namespace='usercenter'),name='usercenter'),  #用户个人中心
    url(r'^apis/',include('apis.urls',namespace='apis'),name='apis'),
    url(r'^master$|^$',views.master,name='master'),
    url(r'^commit/$', views.Commit.as_view(), name='commit'),
    url(r'^high_score/$', views.high_score, name='high_score'),
    url(r'^category/(?P<keywords>\w+)$', views.category, name='category'),
    url(r'^search/$', views.search, name='search'),
    url(r'^comment/(?P<id>\d+)$',views.comment,name='comment'),
    url(r'^reviews/(?P<id>\d+)$', views.reviews,name='reviews'),
    url(r'^about/$',views.about,name='about'),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEIDA_ROOT}),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
]
