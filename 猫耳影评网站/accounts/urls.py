from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.Login.as_view(),name='login'),
    url(r'^registe/$', views.Registe.as_view(),name='registe'),
    url(r'^logout/$', views.logout,name='logout'),
]