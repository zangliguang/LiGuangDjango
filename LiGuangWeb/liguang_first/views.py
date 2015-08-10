# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
# import datetime
# Create your views here.
from models import BusinessClass


def bclist(request):
    BusinessClasslist = BusinessClass.objects.all()
    return render(request, 'liguang_first/bc_list_view.html',
                  {'BusinessClasslist': BusinessClasslist})


def rendertoHome(request):
    # user baidu as homePage
    return HttpResponseRedirect("http://www.baidu.com/")
