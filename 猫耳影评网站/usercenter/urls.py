from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
urlpatterns = [
   url('^base/$',TemplateView.as_view(template_name='uc_base.html'),name='base'),
   url('^profile/$',views.Profile.as_view(),name='profile'),
   url('^contribute/$',views.Contribute.as_view(),name='contribute'),
   url('^collect/$',views.Collect.as_view(),name='collect'),
]