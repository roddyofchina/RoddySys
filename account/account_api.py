#coding:utf8
__author__ = 'Di LUO'

from django.http import HttpResponseRedirect

def require_login(func):
    """要求登录的装饰器"""
    def _deco(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return HttpResponseRedirect('/account/login/')
        return func(request, *args, **kwargs)
    return _deco
