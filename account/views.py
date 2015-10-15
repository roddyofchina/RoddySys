#coding:utf8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from account_api import *
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt


from django.contrib import auth
from account.models import *
from django.core.context_processors import csrf


def login_user(request):
    if request.session.get('user_name', False):
        return HttpResponseRedirect('/')

    if request.method == 'GET':

        return render_to_response('account/login.html', RequestContext(request))

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        if user and user.is_active:
            auth.login(request, user)
            request.session['user_name'] = user.username
            request.session['user_role'] = user.role
            request.session['user_id'] = user.id
            return HttpResponseRedirect("/")
        else:

            kwvars = {
                'request': request,
                'have_error_data': "用户名或密码错误"
            }
            return render_to_response("account/login.html", kwvars, RequestContext(request))


def logout_user(request):
    auth.logout(request)
    if request.session.get('user_name'):
        del request.session['user_name']
    return HttpResponseRedirect("/")


@require_login
def account_list(request):

    GetUser = get_user_model().objects.all()
    Username=request.session.get('user_name')

    kwvars = {
        'request': request,
        'GetUser': GetUser,
        'list_role': list_role,
        'username': Username,
    }


    return render_to_response('account/user_list.html',kwvars,RequestContext(request))



@require_login
def account_add(request):
    if request.method == 'GET':
        Deptlist = Dept.objects.all()
        Username=request.session.get('user_name')
        kwvars = {
            'request': request,
            'Deptlist': Deptlist,
            'list_role': list_role,
            'username': Username,
        }
        return render_to_response('account/user_add.html',kwvars,RequestContext(request))

    if request.method == 'POST':
        user_name = request.POST.get('username')
        if is_common_user(request):
            return HttpResponse("普通用户没有权限!!!")
        if User.objects.filter(username=user_name):
            return HttpResponse("用户已经存在!!!")
        else:
            pass_wd = request.POST.get('passwd')
            pass_wd = make_password(pass_wd)
            email_name = request.POST.get('email')
            sex_name = request.POST.get('sex')
            dept = request.POST.get('dept')
            dept_name = Dept.objects.get(id=dept)
            nick_name = request.POST.get('nickname')
            phone = request.POST.get('phone')
            role_name = request.POST.get('role')
            isactive = request.POST.get('isactive')
            p=User(username=user_name, password=pass_wd, email=email_name, sex=sex_name, dept=dept_name,\
                   nickname=nick_name, role=role_name, is_active=isactive, phone=phone
                   )
            p.save()
            return HttpResponse("用户添加成功")




@require_login
def account_edit(request,id):
    if request.method == 'GET':
        Userinfo=User.objects.filter(id=id)
        Username=request.session.get('user_name')
        Deptlist=Dept.objects.all()
        kwvars = {
            'request': request,
            'Userinfo': Userinfo,
            'list_role': list_role,
            'Deptlist': Deptlist,
            'username': Username,
        }
        return render_to_response('account/user_edit.html',kwvars,RequestContext(request))

    if request.method == 'POST':
            if is_common_user(request):
                return HttpResponse("普通用户没有权限!!!")
            Useredit =User.objects.get(id=id)
            Useredit.username = request.POST.get('username')
            Useredit.email = request.POST.get('email')
            Useredit.sex = request.POST.get('sex')
            dept = request.POST.get('dept')
            Useredit.dept = Dept.objects.get(id=dept)
            Useredit.nickname = request.POST.get('nickname')
            Useredit.phone = request.POST.get('phone')
            Useredit.role = request.POST.get('role')
            Useredit.is_active = int(request.POST.get('isactive')) #数据库类型为int所以要进行转换
            Useredit.save()
            return HttpResponse("用户修改成功")

@require_login
def account_del(request,id):
    if is_common_user(request):
        return HttpResponse("普通用户没有权限!!!")
    if id == '1':
        return HttpResponse(u'超级管理员不能删除')
    else:
        get_user_model().objects.get(id=id).delete()
    return HttpResponse(u'用户删除成功!!!')


@require_login
def dept_list(request):
    DeptData=Dept.objects.all()
    if request.method == 'GET':
        Deptlist=Dept.objects.all()
        Username=request.session.get('user_name')
        kwvars = {
            'request': request,
            'Deptlist': Deptlist,
            'username': Username,
        }
        return render_to_response('account/dept_list.html',kwvars,RequestContext(request))


@require_login
def dept_add(request):
    if  request.method == 'GET':
        Username=request.session.get('user_name')
        kwvars = {
            'request': request,
            'username': Username,
        }
        return render_to_response('account/dept_add.html', kwvars ,RequestContext(request))


    if request.method == 'POST':
        dept_name=request.POST.get('dept_name')
        if is_common_user(request):
            return HttpResponse("普通用户没有权限!!!")
        if Dept.objects.filter(name=dept_name):

            Warrmess="部门已经存在!!"
            return HttpResponse(Warrmess)
        else:
            p=Dept(name=dept_name)
            p.save()

            return HttpResponse(u"部门添加成功")


@require_login
def dept_edit(request,deid):
    if request.method == 'GET':
        GetDept=Dept.objects.filter(id=deid)
        Username=request.session.get('user_name')
        kwvars = {
            'request': request,
            'GetDept': GetDept,
            'edid': deid,
            'username': Username,
        }
        return render_to_response('account/dept_edit.html', kwvars ,RequestContext(request))

    if request.method == 'POST':
        if is_common_user(request):
            return HttpResponse("普通用户没有权限!!!")

        GetDeptname=request.POST.get('dept_name')
        if not Dept.objects.filter(name=GetDeptname,id=deid):
            return HttpResponse("部门已经存在，请重新输入!!!")
        else:
            GetDept=Dept.objects.get(id=deid)
            GetDept.name=request.POST.get('dept_name')
            GetDept.save()
            return HttpResponse("部门修改成功!!!")


@require_login
def dept_del(request, id):
    if is_common_user(request):
        return HttpResponse("普通用户没有权限!!!")
    if id == '1':
        return HttpResponse(u'默认部门不能删除')
    else:
        Dept.objects.get(id=id).delete()
    return HttpResponseRedirect('/account/dept/list/')


@require_login
def account_detail(request):
    Userinfo = request.session.get('user_name')
    Userdata = User.objects.filter(username=Userinfo)
    kwvars = {
            'request': request,
            'Userdata': Userdata,
            'username': Userinfo,
            'list_role': list_role,
    }
    return render_to_response('account/user_detail.html', kwvars ,RequestContext(request))


@require_login
def set_passwd(request,id):
    Userinfo = request.session.get('user_name')
    Adminrole=User.objects.get(username=Userinfo)
    Uid = Adminrole.role

    if request.method == 'GET':
        UserDATA=User.objects.get(id=id)
        kwvars = {
            'request': request,
            'username': Userinfo,
            'UserDAT': UserDATA,
            'ID': Uid,
        }
        return render_to_response('account/setpasswd.html', kwvars ,RequestContext(request))


    if request.method == 'POST':
        if not is_super_user(request):
            return HttpResponse("超级管理员才可修改密码")

        Userset =User.objects.get(id=id)
        if not Uid ==1:    #如果不是用户超级管理员就进行验证
            oldpasswd=request.POST.get('oldpasswd')   #判断用户输入的当前密码是否正确
            if not Userset.check_password(oldpasswd):
                return HttpResponse("输入的原密码不正确")

        passwd1= request.POST.get('newpasswd1')
        passwd2= request.POST.get('newpasswd2')
        if not passwd2 == passwd1:
            return HttpResponse("您输入的密码不一致!!!!!")
        else:
            Userset.set_password(passwd1)
            Userset.save()
            return HttpResponse("密码修改成功")





