from django.conf.urls import patterns, url
from liguang_first import views
from liguang_first.views import alogout, register2, index

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^login/$', views.alogin, name='alogin'),
                       url(r'^regist/$', views.regist, name='regist'),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^logout/$', views.logout, name='logout'),
                       url(r'^register2/$', register2),
                       url(r'^logout2/$', alogout),  
                       )
