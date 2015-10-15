
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from account.views import *

urlpatterns = patterns('',
  url(r'^login/$',login_user,name='login_user'),
  url(r'^logout/$',logout_user,name='logout_user'),
  url(r'^list/$',account_list,name='account_list'),
  url(r'^add/$',account_add,name='account_add'),
  url(r'^detail/$',account_detail,name='account_detail'),
  url(r'^edit/(\d+)$',account_edit,name='account_edit'),
  url(r'^del/(\d+)$',account_del,name='account_del'),
  url(r'^dept/list/$',dept_list,name='dept_list'),
  url(r'^dept/del/(\d+)$',dept_del,name='dept_del'),
  url(r'^dept/add/$',dept_add,name='dept_add'),
  url(r'^dept/edit/(\d+)$',dept_edit,name='dept_edit'),
  url(r'^setpasswd/(\d+)$',set_passwd,name='set_passwd'),

)