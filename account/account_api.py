#coding:utf8
__author__ = 'Di LUO'

from django.http import HttpResponseRedirect
import os



list_role = {
        1:"超级管理员",
        2:"系统管理员",
        3:"普通用户",
}

server_type = {
        1:"云主机",
        2:"物理机",
        3:"租用机",
}

server_system = {
        1:"Linux",
        2:"windows",
        3:"unix",
}

idc_level={
        1:"高级机房",
        2:"中级机房",
        3:"普通机房"
}

server_status={
        1:"Running",
        2:"Down",
        3:"Unknown"
}




def is_super_user(request):
    if request.session.get('user_role') == 1:
        return True
    else:
        return False


def is_system_admin(request):
    if request.session.get('user_role') == 2:
        return True
    else:
        return False



def is_common_user(request):
    if request.session.get('user_role') == 3:
        return True
    else:
        return False




def require_login(func):
    """要求登录的装饰器"""
    def _deco(request, *args, **kwargs):
        if not request.session.get('user_name'):
            return HttpResponseRedirect('/account/login/')
        return func(request, *args, **kwargs)
    return _deco




def listencelery():
    ps_string = os.popen('ps -ax | grep celery |grep -v grep  ','r').read()
    if len(ps_string) == 0:
        return 1
    else:
        return 0










