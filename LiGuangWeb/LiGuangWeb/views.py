from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
def homePage(req):
     return  HttpResponse("LiGuang HOMEPAGE")
    # return  HttpResponseRedirect("http://www.baidu.com/")