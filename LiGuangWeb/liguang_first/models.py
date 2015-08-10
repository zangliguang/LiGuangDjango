# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import uuid


class UUIDField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 64)
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        if add:
            value = str(uuid.uuid4())
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)


class User(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):           # __unicode__ on Python 2
        return self.username
    # user_id = UUIDField(primary_key=True, editable=False)
    # user_loginname = models.CharField(max_length=32)
    # user_password = models.CharField(max_length=32)
    # value = models.CharField(max_length=255, blank=True)


class BusinessClass(models.Model):
    businessclass_id = UUIDField(primary_key=True, editable=False)
    businessclass_name = models.CharField(max_length=16)
    businessclass_order = models.IntegerField()

    def __unicode__(self):
        return self.businessclass_name


class Business(models.Model):
    business_id = UUIDField(primary_key=True, editable=False)
    business_name = models.CharField(max_length=16)
    business_contents = models.TextField()
    businessclass = models.ForeignKey(BusinessClass)

    def __unicode__(self):
        return self.business_name
