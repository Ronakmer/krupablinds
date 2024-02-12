from django.shortcuts import render

from django.contrib.auth.models import User,auth
from django.conf import settings
from adminSite.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password

import random,math,os,json
from datetime import datetime, timedelta
from datetime import date

# Create your views here.







def dashboard(request):
    return render(request,'adminAppTemplates/dashboard.html')
 


def login_page(request):
    return render(request,'adminAppTemplates/login.html')
 