#coding:utf8
from django.db import models
from account.models import Dept




class zone(models.Model):
    name = models.CharField(max_length=50,default="北京")
    comment = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class idclist(models.Model):
    idcname = models.CharField(max_length=50)
    idczone = models.ForeignKey(zone,null=True, blank=True)
    idclevel = models.IntegerField(max_length=11,null=True)
    idcdesc = models.CharField(max_length=255)
    idcaddr = models.CharField(max_length=500)
    def __unicode__(self):
        return self.idcname


class business(models.Model):
    name = models.CharField(max_length=50)
    contactperson = models.CharField(max_length=50,null=True)
    contactphone = models.CharField(max_length=50,null=True)
    contactemail = models.CharField(max_length=50,null=True)
    def __unicode__(self):
        return self.name

class servers(models.Model):
    hostname = models.CharField(max_length=100)
    externalip = models.CharField(max_length=150)
    internalip = models.CharField(max_length=150)
    virtip = models.CharField(max_length=150)
    businessname = models.ForeignKey(business, null=True, blank=True)
    passwd = models.CharField(max_length=150)
    dept = models.ForeignKey(Dept,null=True,blank=True)
    cpu = models.CharField(max_length=50,null=True)
    cpumhz = models.CharField(max_length=50,null=True)
    mem = models.CharField(max_length=50,null=True)
    disk = models.CharField(max_length=50,null=True)
    idc = models.ForeignKey(idclist, null=True,blank=True)
    type = models.IntegerField(max_length=11,null=True)
    status = models.IntegerField(max_length=11,null=True,default=3)
    system = models.IntegerField(max_length=11,null=True)
    addtime = models.DateTimeField(auto_now_add=True,null=True)
    comment = models.TextField(blank=True, null=True,max_length=500)

    def __unicode__(self):
        return self.hostname
