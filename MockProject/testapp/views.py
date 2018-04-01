# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import HttpResponse
import models


# Create your views here.

user_list = [
    {"user":"jiangtao","pwd":"123456"},
    {"user":"steven","pwd":"654321"},
]


def index(request):
    #return HttpResponse("tgt mock ,start!")
    #global user_list
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        #print (username, password)
       #models.UserInfo.objects.create(user=username,pwd=password)
        #user_list = models.UserInfo.objects.all()
        #temp = {"user":username,"pwd":password}
        #user_list.append(temp)

    return render(request, "index.html",{"data": user_list})