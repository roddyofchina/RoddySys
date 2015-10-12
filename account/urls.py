
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from account.views import *

urlpatterns = patterns('',
  url(r'^login/$',login_user,name='login_user'),
  url(r'^logout/$',logout_user,name='logout_user'),
  url(r'^list/$',account_list,name='account_list'),
  url(r'^add/$',account_add,name='account_add'),
  url(r'^dept/list/$',dept_list,name='dept_list'),
)