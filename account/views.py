#coding:utf8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext



from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf



def login_user(request):
    if request.session.get('user_id',False):
        return HttpResponseRedirect('/')

    if request.method == 'GET':

        return render_to_response('account/login.html',RequestContext(request))

    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)

        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)

        if user and user.is_active:
            auth.login(request, user)
            request.session['user_id'] = user.id
            return HttpResponseRedirect("/")
        else:

            kwvars = {
                'request':request,
                'have_error_data':"用户名或密码错误"
            }
            return render_to_response("account/login.html",kwvars,RequestContext(request))



def logout_user(request):
    auth.logout(request)
    if request.session.get('user_id'):
        del request.session['user_id']
    return HttpResponseRedirect("/")




def account_list(request):

    return render_to_response('account/user_list.html')


def account_add(request):
    return render_to_response('account/user_add.html')


def dept_list(request):
    return render_to_response('account/dept_list.html')


