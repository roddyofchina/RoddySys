from django.shortcuts import render,render_to_response
from django.http import HttpResponse




def domain_list(request):
    return render_to_response('domainsys/domain_list.html')


def domain_add(request):
    return render_to_response('domainsys/domain_add.html')


def domain_edit(request):
    return render_to_response('domainsys/domain_eidt.html')


def domain_del(request):
    return HttpResponse('domain del')


def provider_list(request):
    return  render_to_response('domainsys/provider_list.html')


def provider_add(request):
    return  render_to_response('domainsys/provider_add.html')


def provider_edit(request):
    return  render_to_response('domainsys/provider_edit.html')


def domain_expire(request):
    return  render_to_response('domainsys/expire.html')
