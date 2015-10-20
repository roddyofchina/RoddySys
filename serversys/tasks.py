#coding:utf8
from celery import shared_task
import multiprocessing,subprocess
import django
django.setup()
from serversys.models import *


def Serverping(ip,q,r):
    getdata=subprocess.call("ping -c 3 -W 3 " + ip,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    )
    if getdata == 0:
        q.put("Ping Successful!!")
    r.put('%s;%s'%(ip,getdata))


@shared_task
def runping():
    servers_ip=servers.objects.values_list('externalip')
    q = multiprocessing.Queue()     #生成两个队列
    r = multiprocessing.Queue()
    total=[]
    count=0
    for IP in servers_ip:
        p = multiprocessing.Process(target=Serverping, args=(IP[0],q,r))
        count +=1
        p.start()
        total.append(p)
    for j in total:
        j.join()

    for j in total:
        getvalue=r.get().split(';')
        ip=getvalue[0]
        status_code=getvalue[1]
        status_old=servers.objects.get(externalip=ip)
        if status_code == "1":
            status_old.status = 2
            status_old.save()
        else:
            status_old.status = 1
            status_old.save()
    return "running:%s,down:%s" %(q.qsize(),count - q.qsize())






