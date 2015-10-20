#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext

from account.account_api import *
from account.models import *
from serversys.models import *
from django.contrib import auth

import base64
import json
import xlwt
import StringIO

import time,datetime


@require_login
def index(request):
    if request.method =='GET':
        Username=request.session.get('user_name')
        IDCdata=idclist.objects.all().count()
        Userdata=User.objects.all().count()
        ServerData=servers.objects.all().count()

        kwvars = {
            'request': request,
            'username': Username,
            'IDCdata':IDCdata,
            'Userdata':Userdata,
            'ServerData':ServerData,

        }
        return  render_to_response('index.html',kwvars,RequestContext(request))



@require_login
def server_lists(request):
    if request.method =='GET':
        Username=request.session.get('user_name')
        Serverlist= servers.objects.all()
        kwvars = {
            'request': request,
            'username': Username,
            'Serverlist':Serverlist,
            'ServerStatus': server_status,
        }
        return render_to_response('serversys/server_lists.html',kwvars,RequestContext(request))


@require_login
def server_add(request):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        Deptdata=Dept.objects.all()
        Businessdata=business.objects.all()
        Idcdata=idclist.objects.all()
        kwvars = {
            'request': request,
            'username': Username,
            'Deptdata': Deptdata,
            'Businessdata': Businessdata,
            'Idcdata': Idcdata,
            'ServerType': server_type,
            'Server_system': server_system,
        }
        return render_to_response('serversys/server_add.html',kwvars,RequestContext(request))

    if request.method == 'POST':
        hostname = request.POST.get('servername')
        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")
        if servers.objects.filter(hostname=hostname):
            return HttpResponse(u"主机已经存在!!!")
        else:
            pass_wd = request.POST.get('passwd')
            passwd = base64.encodestring(pass_wd)
            externalip = request.POST.get('externalip')
            internalip = request.POST.get('internalip')
            vip = request.POST.get('vip')
            Business_id = request.POST.get('Business')
            Business = business.objects.get(id=Business_id)
            dept_id = request.POST.get('dept')
            deptname = Dept.objects.get(id=dept_id)
            cpu = request.POST.get('cpu')
            cpumhz = request.POST.get('cpumhz')
            mem = request.POST.get('mem')
            disk = request.POST.get('disk')
            type = request.POST.get('type')
            system = request.POST.get('system')
            desc = request.POST.get('desc')
            idc_id = request.POST.get('idc')
            idc=idclist.objects.get(id=idc_id)
            p=servers(hostname=hostname,externalip=externalip,internalip=internalip,businessname=Business,\
                      passwd=passwd,dept=deptname,cpu=cpu,cpumhz=cpumhz,mem=mem,disk=disk,type=type,system=system,comment=desc,\
                      idc=idc,virtip=vip
                   )
            p.save()
            return HttpResponse(u"主机添加成功")




@require_login
def server_alladd(request):

      if request.method == 'POST':
            ServerDatalists = request.POST.get('addallserver')
            GetServerData=ServerDatalists.split('\n')

            errormsg=[]
            countcode=0
            for s in GetServerData:
                count = {}
                s = s.split('|')
                hostname=s[0]
                hostnameid=servers.objects.filter(hostname=hostname)
                if hostnameid:
                    count[s[0]]="主机名已经存在"
                    errormsg.append(count)
                    continue

                externalip=s[1]
                internalip=s[2]
                vip=s[3]
                Business_id=s[4]
                Businessname = business.objects.filter(name=Business_id)
                if not Businessname:

                    count[s[0]]="业务不存在"
                    errormsg.append(count)

                    continue
                else:
                     Businessnameid = business.objects.get(name=Business_id)

                dept_id=s[5]
                deptname = Dept.objects.filter(name=dept_id)
                if not deptname:
                    count[s[0]]="部门不存在"
                    errormsg.append(count)

                    continue
                else:
                     deptnameid = Dept.objects.get(name=dept_id)

                cpu=s[6]
                cpumhz=s[7]
                mem=s[8]
                disk=s[9]
                type=s[10]
                system=s[11]
                idc_id=s[12]

                idcnamedd = idclist.objects.filter(idcname=idc_id)

                if not idcnamedd:
                    count[s[0]]="IDC不存在"
                    errormsg.append(count)
                    continue
                else:
                    idcnameid = idclist.objects.get(idcname=idc_id)

                pass_wd=s[13]
                desc=s[14]
                passwd = base64.encodestring(pass_wd)

                countcode+=1

                p=servers(hostname=hostname,externalip=externalip,internalip=internalip,businessname=Businessnameid,\
                  passwd=passwd,dept=deptnameid,cpu=cpu,cpumhz=cpumhz,mem=mem,disk=disk,type=type,system=system,comment=desc,\
                  idc=idcnameid,virtip=vip
                )
                p.save()

            if len(count) == 0:
                return HttpResponse(u"批量添加主机成功")
            else:
                return HttpResponse(json.dumps(errormsg), content_type="application/json")

            '''
            if is_common_user(request):
                return HttpResponse(u"普通用户没有权限!!!")
            if servers.objects.filter(hostname=hostname):
                return HttpResponse(u"主机已经存在!!!")
            else:
                pass_wd = request.POST.get('passwd')
                passwd = base64.encodestring(pass_wd)
                externalip = request.POST.get('externalip')
                internalip = request.POST.get('internalip')
                vip = request.POST.get('vip')
                Business_id = request.POST.get('Business')
                Business = business.objects.get(id=Business_id)
                dept_id = request.POST.get('dept')
                deptname = Dept.objects.get(id=dept_id)
                cpu = request.POST.get('cpu')
                cpumhz = request.POST.get('cpumhz')
                mem = request.POST.get('mem')
                disk = request.POST.get('disk')
                type = request.POST.get('type')
                system = request.POST.get('system')
                desc = request.POST.get('desc')
                idc_id = request.POST.get('idc')
                idc=idclist.objects.get(id=idc_id)
                p=servers(hostname=hostname,externalip=externalip,internalip=internalip,businessname=Business,\
                          passwd=passwd,dept=deptname,cpu=cpu,cpumhz=cpumhz,mem=mem,disk=disk,type=type,system=system,comment=desc,\
                          idc=idc,virtip=vip
                       )
                p.save()
                '''






@require_login
def server_edit(request,id):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        ServerData= servers.objects.get(id= id)
        Deptdata=Dept.objects.all()
        Businessdata=business.objects.all()
        Idcdata=idclist.objects.all()
        passwd=base64.decodestring(ServerData.passwd)
        kwvars = {
            'request': request,
            'username': Username,
            'Deptdata': Deptdata,
            'Businessdata': Businessdata,
            'Idcdata': Idcdata,
            'ServerType': server_type,
            'Passwd': passwd,
            'Server_system': server_system,
            'ServerData':ServerData

        }
        return render_to_response('serversys/server_edit.html',kwvars,RequestContext(request))

    if request.method == 'POST':
            if is_common_user(request):
                return HttpResponse(u"普通用户没有权限!!!")
            Serveredit =servers.objects.get(id=id)
            Serveredit.hostname = request.POST.get('servername')
            pass_wd = request.POST.get('passwd')
            Serveredit.passwd = base64.encodestring(pass_wd)
            Serveredit.externalip = request.POST.get('externalip')
            Serveredit.internalip = request.POST.get('internalip')
            Serveredit.vip = request.POST.get('vip')
            Business_id = request.POST.get('Business')
            Serveredit.businessname = business.objects.get(id=Business_id)
            dept_id = request.POST.get('dept')
            Serveredit.dept = Dept.objects.get(id=dept_id)
            Serveredit.cpu = request.POST.get('cpu')
            Serveredit.cpumhz = request.POST.get('cpumhz')
            Serveredit.mem = request.POST.get('mem')
            Serveredit.disk = request.POST.get('disk')
            Serveredit.type = request.POST.get('type')
            Serveredit.system = request.POST.get('system')
            Serveredit.desc = request.POST.get('desc')
            idc_id = request.POST.get('idc')
            Serveredit.idc=idclist.objects.get(id=idc_id)
            Serveredit.save()
            return HttpResponse(u"修改成功")


@require_login
def server_detail(request,id):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        ServerData= servers.objects.filter(id=id)

        kwvars = {
            'request': request,
            'username': Username,
            'ServerData':ServerData,
            'Server_system':server_system,
            'Server_type':server_type,
            'ServerStatus': server_status,
        }

        return render_to_response('serversys/server_detail.html',kwvars,RequestContext(request))

@require_login
def server_del(request,id):
    if request.method == 'GET':
        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")
        servers.objects.get(id=id).delete()
        return HttpResponse(u'主机删除成功!!')



@require_login
def display_pass(request,id):
    if request.method == 'GET':
        Serverone=servers.objects.get(id=id)
        echopasswd=base64.decodestring(Serverone.passwd)

        return HttpResponse(echopasswd)


@require_login
def idc_list(request):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        Idclists= idclist.objects.all()

        idcdict={}
        for v in Idclists:
            csd=servers.objects.filter(idc=v.id).count()
            idcdict[v.id]=csd
        kwvars = {
            'request': request,
            'username': Username,
            'Idclists': Idclists,
            'idcdict': idcdict,
            'Idclevel': idc_level,
        }
        return render_to_response('idcmanage/idc_list.html',kwvars,RequestContext(request))


@require_login
def idc_other(request,id):
    if request.method == 'GET':
        data={}
        idcdataother=idclist.objects.get(id=id)
        data["desc"]=idcdataother.idcdesc
        data["addr"]=idcdataother.idcaddr
        return HttpResponse(json.dumps(data), content_type="application/json")


@require_login
def idc_add(request):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        ZoneD = zone.objects.all()
        kwvars = {
            'request': request,
            'username': Username,
            'ZoneData': ZoneD,
            'Idclevel': idc_level,
        }
        return render_to_response('idcmanage/idc_add.html', kwvars ,RequestContext(request))



    if request.method == 'POST':
        idc_name = request.POST.get('idcname')
        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")
        if idclist.objects.filter(idcname=idc_name):
            Warrmess = u"IDC名已经存在!!"
            return HttpResponse(Warrmess)
        else:
            desc = request.POST.get('desc')
            zoned = request.POST.get('zone')
            zoned = zone.objects.get(id=zoned)
            level = request.POST.get('level')
            addr = request.POST.get('addr')

            p = idclist(idcname=idc_name, idczone=zoned, idclevel=level, idcdesc=desc, idcaddr=addr)
            p.save()

            return HttpResponse(u"IDC添加成功")

@require_login
def idc_edit(request,id):
    if request.method == 'GET':
        idcdata=idclist.objects.get(id=id)
        Username=request.session.get('user_name')
        ZoneData=zone.objects.all()
        kwvars = {
            'request': request,
            'idcdata': idcdata,
            'username': Username,
            'Idclevel': idc_level,
            'ZoneData': ZoneData,
        }
        return render_to_response('idcmanage/idc_edit.html', kwvars ,RequestContext(request))

    if request.method == 'POST':
        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")

        idc_name=request.POST.get('idcname')

        if idclist.objects.filter(idcname=idc_name,id=id):
            idcdata=idclist.objects.get(id=id)
            idcdata.idcname=idc_name
            idcdata.idcdesc = request.POST.get('desc')
            zoned = request.POST.get('zone')
            idcdata.idczone = zone.objects.get(id=zoned)
            idcdata.idclevel = request.POST.get('level')
            idcdata.idcaddr = request.POST.get('addr')
            idcdata.save()
            return HttpResponse(u"IDC修改成功!!!")

        if idclist.objects.filter(idcname=idc_name):
            return HttpResponse(u"IDC已经存在，请重新输入!!!")
        else:
            idcdata=idclist.objects.get(id=id)
            idcdata.idcname=idc_name
            idcdata.idcdesc = request.POST.get('desc')
            zoned = request.POST.get('zone')
            idcdata.idczone = zone.objects.get(id=zoned)
            idcdata.idclevel = request.POST.get('level')
            idcdata.idcaddr = request.POST.get('addr')
            idcdata.save()
            return HttpResponse(u"IDC修改成功!!!")


@require_login
def idc_del(request,id):
    idcdata = idclist.objects.get(id=id)
    if is_common_user(request):
        return HttpResponse(u"普通用户没有权限!!!")
    if idcdata.servers_set.all():
        return HttpResponse(u'IDC不能删除，请删除关联服务器')
    else:
        idclist.objects.get(id=id).delete()
    return HttpResponse(u"IDC删除成功!!!")

@require_login
def zone_list(request):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        Zonelist= zone.objects.all()

        kwvars = {
            'request': request,
            'username': Username,
            'ZoneData': Zonelist,
        }
        return render_to_response('zonemanage/zone_list.html',kwvars,RequestContext(request))


@require_login
def zone_add(request):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        kwvars = {
            'request': request,
            'username': Username,
        }
        return render_to_response('zonemanage/zone_add.html', kwvars ,RequestContext(request))
    if request.method == 'POST':
        zone_name=request.POST.get('zone_name')
        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")
        if zone.objects.filter(name=zone_name):
            Warrmess=u"区域名已经存在!!"
            return HttpResponse(Warrmess)
        else:
            p=zone(name=zone_name)
            p.save()

            return HttpResponse(u"区域添加成功")

@require_login
def zone_edit(request,id):
    if request.method == 'GET':
        zonedata=zone.objects.get(id=id)
        Username=request.session.get('user_name')
        kwvars = {
            'request': request,
            'zonedata': zonedata,
            'edid': id,
            'username': Username,
        }
        return render_to_response('zonemanage/zone_edit.html', kwvars ,RequestContext(request))

    if request.method == 'POST':

        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")

        Zonename=request.POST.get('zone_name')
        if zone.objects.filter(name=Zonename,id=id):

            zonedata=zone.objects.get(id=id)
            zonedata.name=request.POST.get('zone_name')
            zonedata.save()
            return HttpResponse(u"区域修改成功!!!")

        if zone.objects.filter(name=Zonename):
            return HttpResponse(u"区域名已经存在，请重新输入!!!")
        else:
            zonedata=zone.objects.get(id=id)
            zonedata.name=request.POST.get('zone_name')
            zonedata.save()
            return HttpResponse(u"区域修改成功!!!")

@require_login
def zone_del(request,id):
    idczone = zone.objects.get(id=id)

    if is_common_user(request):
        return HttpResponse(u"普通用户没有权限!!!")
    if id == '1':
        return HttpResponse(u'默认区域不能删除')
    if idczone.idclist_set.all():
        return HttpResponse(u'区域不能删除，请删除关联IDC')
    else:
        zone.objects.get(id=id).delete()
    return HttpResponse(u"区域删除成功!!!")


@require_login
def Business_list(request):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        BusinessData=business.objects.all()
        kwvars = {
            'request': request,
            'username': Username,
            'BusinessData': BusinessData,
        }
        return render_to_response('Business/Business_list.html',kwvars,RequestContext(request))

@require_login
def Business_add(request):
    if request.method == 'GET':
        Username=request.session.get('user_name')
        kwvars = {
            'request': request,
            'username': Username,
        }
        return render_to_response('Business/Business_add.html', kwvars ,RequestContext(request))

    if request.method == 'POST':
        businessname=request.POST.get('name')


        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")
        if business.objects.filter(name=businessname):
            Warrmess=u"业务已经存在!!"
            return HttpResponse(Warrmess)
        else:
            contactperson=request.POST.get('contactperson')
            contactemail=request.POST.get('contactemail')
            contactphone=request.POST.get('contactphone')
            p=business(name=businessname,contactperson=contactperson,contactemail=contactemail,contactphone=contactphone)
            p.save()
            return HttpResponse(u"业务添加成功")





@require_login
def Business_edit(request,id):
    if request.method == 'GET':
        Businessdata=business.objects.get(id=id)
        Username=request.session.get('user_name')
        kwvars = {
            'request': request,
            'Businessdata': Businessdata,
            'username': Username,
        }
        return render_to_response('Business/Business_edit.html', kwvars ,RequestContext(request))

    if request.method == 'POST':
        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")

        Businessdata=request.POST.get('name')

        print request.POST.get('contactemail')
        if business.objects.filter(name=Businessdata,id=id):

            busdata=business.objects.get(id=id)
            busdata.name=request.POST.get('name')
            busdata.contactperson=request.POST.get('contactperson')
            busdata.contactphone=request.POST.get('contactphone')
            busdata.contactemail=request.POST.get('contactemail')
            busdata.save()
            return HttpResponse(u"业务修改成功!!!")
        if business.objects.filter(name=Businessdata):
            return HttpResponse(u"业务名已经存在，请重新输入!!!")
        else:
            busdata=business.objects.get(id=id)
            busdata.name=request.POST.get('name')
            busdata.contactperson=request.POST.get('contactperson')
            busdata.contactphone=request.POST.get('contactphone')
            busdata.contactemail=request.POST.get('contactemail')
            busdata.save()
            return HttpResponse(u"业务修改成功!!!")


@require_login
def Business_del(request,id):
    Businessdata = business.objects.get(id=id)

    if is_common_user(request):
        return HttpResponse(u"普通用户没有权限!!!")
    if id == '1':
        return HttpResponse(u'默认业务不能删除')
    if Businessdata.servers_set.all():
        return HttpResponse(u'业务不能删除，请删除关联主机')
    else:
        business.objects.get(id=id).delete()
    return HttpResponse(u"业务删除成功!!!")



@require_login
def exportAgencyCustomers(request):
    datenow=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
    file=datenow+"主机状态.xls"
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' %file
    wb = xlwt.Workbook(encoding = 'utf-8')

    sheet = wb.add_sheet(str(datenow)+" 主机状态",cell_overwrite_ok=True)
    #1st line
    sheet.write(0,0, 'ID')
    sheet.write(0,1, '主机')
    sheet.write(0,2, '外网IP')
    sheet.write(0,3, '内网IP')
    sheet.write(0,4, '虚拟IP')
    sheet.write(0,5, '业务')
    sheet.write(0,6, '部门')
    sheet.write(0,7, 'CPU')
    sheet.write(0,8, 'Mem')
    sheet.write(0,9, 'Disk')
    sheet.write(0,10, '机房')
    sheet.write(0,11, '区域')
    sheet.write(0,12, '主机类型')
    sheet.write(0,13, '主机系统')
    sheet.write(0,14, '说明')
    sheet.write(0,15, '状态')
    sheet.write(0,16, '添加时间')
    row = 1
    for server in servers.objects.all():

        sheet.write(row,0, server.id)
        sheet.write(row,1, server.hostname)
        sheet.write(row,2, server.externalip)
        sheet.write(row,3, server.internalip)
        sheet.write(row,4, server.virtip)
        sheet.write(row,5, server.businessname.name)
        sheet.write(row,6, server.dept.name)
        sheet.write(row,7, server.cpu)
        sheet.write(row,8, server.mem)
        sheet.write(row,9, server.disk)
        sheet.write(row,10, server.idc.idcname)
        sheet.write(row,11, server.idc.idczone.name)
        sheet.write(row,12, server.type)
        sheet.write(row,13, server.system)
        sheet.write(row,14, server.comment)
        addtimes = datetime.datetime.strftime(server.addtime, '%Y-%m-%d %H:%M:%S')
        if server.status == 1:
            status = 'Running'
        elif server.status == 2:
            status = 'Down'
        else:
            status = 'Unknown'
        sheet.write(row,15, status)
        sheet.write(row,16, str(addtimes))
        row=row + 1
    output = StringIO.StringIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response










