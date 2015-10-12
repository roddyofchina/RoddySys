from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from serversys.views import *
from domainsys.views import *



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RoddySys.views.home', name='home'),
    url(r'^account/', include('account.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','serversys.views.index',name='index'),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,}),
)

urlpatterns += patterns('serversys',
    url(r'^server/server_lists/$',server_lists,name='server_list'),
    url(r'^server/add/$',server_add,name='server_add'),
    url(r'^server/del/$',server_del,name='server_del'),
    url(r'^server/edit/$',server_edit,name='server_edit'),
    url(r'^server/server_detail/$',server_detail,name='server_edit'),
    url(r'^idc/list/$',idc_list,name='idc_list'),
    url(r'^idc/add/$',idc_add,name='idc_add'),
    url(r'^idc/del/$',idc_del,name='idc_del'),
    url(r'^idc/edit/$',idc_edit,name='idc_edit'),
    url(r'^zone/list/$',zone_list,name='zone_list'),
    url(r'^zone/add/$',zone_add,name='zone_add'),
    url(r'^zone/del/$',zone_del,name='zone_del'),
    url(r'^zone/edit/$',zone_edit,name='zone_edit'),

    url(r'^Business/list/$',Business_list,name='Business_list'),
    url(r'^Business/add/$',Business_add,name='Business_add'),
    url(r'^Business/del/$',Business_del,name='Business_del'),
    url(r'^Business/edit/$',Business_edit,name='Business_edit'),
)

urlpatterns += patterns('domainsys',
    url(r'^domain/list/$',domain_list,name='domain_list'),
    url(r'^domain/add/$',domain_add,name='domain_add'),
    url(r'^domain/del/$',domain_del,name='domain_del'),
    url(r'^domain/edit/$',domain_edit,name='domain_edit'),
    url(r'^domain/expire/$',domain_expire,name='domain_expire'),
    url(r'^provider/list/$',provider_list,name='provider_list'),
    url(r'^provider/add/$',provider_add,name='provider_add'),
    url(r'^provider/edit/$',provider_edit,name='provider_edit'),
)


