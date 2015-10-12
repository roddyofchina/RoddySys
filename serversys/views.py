from django.shortcuts import render,render_to_response
from django.http import HttpResponse

from account.account_api import require_login
from django.contrib import auth


@require_login
def index(request):
    if request.method =='GET':
        return  render_to_response('index.html')


def server_lists(request):
    return render_to_response('serversys/server_lists.html')


def server_add(request):
    return render_to_response('serversys/server_add.html')


def server_edit(request):
    return render_to_response('serversys/server_edit.html')


def server_detail(request):
    return render_to_response('serversys/server_detail.html')


def server_del(request):
    return HttpResponse('servers del')


def idc_list(request):
    return render_to_response('idcmanage/idc_list.html')


def idc_add(request):
    return render_to_response('idcmanage/idc_add.html')


def idc_edit(request):
    return render_to_response('idcmanage/idc_eidt.html')


def idc_del(request):
    return HttpResponse('idc del')


def zone_list(request):
    return render_to_response('zonemanage/zone_list.html')



def zone_add(request):
    return render_to_response('zonemanage/zone_add.html')



def zone_edit(request):
    return render_to_response('zonemanage/zone_edit.html')


def zone_del(request):
    return HttpResponse('zone del')



def Business_list(request):
    return render_to_response('Business/Business_list.html')



def Business_add(request):
    return render_to_response('Business/Business_add.html')



def Business_edit(request):
    return render_to_response('Business/Business_edit.html')


def Business_del(request):
    return HttpResponse('Business del')










