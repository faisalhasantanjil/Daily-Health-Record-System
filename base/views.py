
# from urllib.request import Request
import email
import math
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#
from .forms import CreateUserForm, HealthInfoForm, UserInformationForm, RecordFileForm
from .models import *

# Create your views here.


@login_required(login_url='loginuser')
def home(request):
    user = request.user
    context = {'user': user}
    return render(request, 'base/home.html', context)


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username," and ", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'base/loginuser.html', context)


def logoutuser(request):
    logout(request)
    return redirect('loginuser')


def registeruser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # request.POST['username'] = request.POST['email']
        form.instance.username = request.POST['email']
        print(form.instance.username)
        print(form)
        if form.is_valid():
            print(form.instance.username)
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(
                request, 'Account has been registered. Email: ' + email)
            login(request, form.save())
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/registeruser.html', context)


def userinfo(request):

    form = UserInformationForm()
    print(form)
    user_email = request.user.email
    print(f'Hello there {user_email}')
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        feet = request.POST['feetheight']
        inch = request.POST['inchheight']
        height = (float(feet)*30.48)+(float(inch)*2.54)
        form.instance.email = user_email
        form.instance.height = height
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/userinfo.html', context)


@login_required(login_url='loginuser')
def addrecord(request):
    user_email = request.user.email
    users = UserInformation.objects.values()
    valid_users = list(users)
    print(type(valid_users))
    for valid_user in valid_users:
        print(valid_user)
        # if valid_user.email == user_email:
        #     return redirect('bmicalculate')

    form = RecordFileForm()
    # patient = UserInformation.objects.get(email=user_email)
    # print(patient)
    if request.method == 'POST':
        form = RecordFileForm(request.POST, request.FILES)
        form.instance.email = user_email
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/addrecord.html', context)


@login_required(login_url='loginuser')
def viewrecord(request):
    user_email = request.user.email
    records = RecordFile.objects.filter(email=user_email)
    print(records.datetimes)
    # print(records.__dict__.keys())
    context = {'records': records}
    return render(request, 'base/viewrecord.html', context)

# def menu(request):
#     return render(request, 'menu.html')


def bmicalculate(request):
    if request.method == 'POST':
        feet = request.POST['feetheight']
        inch = request.POST['inchheight']
        height = (float(feet)*30.48)+(float(inch)*2.54)
        weight = request.POST['weight']
        bmi = float("{:.3f}".format(float(weight) /
                    ((float(height)/100)*(float(height)/100))))
        below = False
        good = False
        above = False
        obsess = False
        if bmi < 25:
            good = True
        if bmi > 25:
            above = True
        context = {'bmi': bmi, 'good': good, 'above': above
                   }
        return render(request, 'base/bmiresult.html', context)
        # return redirect('bmiresult', context)
    context = {}
    return render(request, 'base/bmicalculate.html', context)


def bmiresult(request):

    context = {}
    return render(request, 'base/bmicalculate.html', context)


def addhealthinfo(request):
    form = HealthInfoForm()
    user_email = request.user.email
    healthinfos = HealthInfo.objects.filter(email=user_email)
    if request.method == 'POST':
        form = HealthInfoForm(request.POST)
        form.instance.email = user_email
        if form.is_valid():
            form.save()
            return redirect('addhealthinfo')

    context = {'form': form, 'healthinfos': healthinfos}
    return render(request, 'base/addhealthinfo.html', context)
