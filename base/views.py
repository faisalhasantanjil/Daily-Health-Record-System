
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
from .forms import CreateUserForm, DietRecordForm, ExerciseRecordForm, HealthInfoForm, UserInformationForm, RecordFileForm
from .models import *

# Create your views here.


@login_required(login_url='loginuser')
def home(request):
    user = request.user
    user_email = request.user.email
    userinfo = UserInformation.objects.filter(email=user_email)
    print(userinfo)

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')

    context = {'user': user, 'userinfo': userinfo}
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
        # print(form.instance.username)
        # print(form)
        if form.is_valid():
            # print(form.instance.username)
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
    # print(form)
    user_email = request.user.email
    # print(f'Hello there {user_email}')
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

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')

    # print(type(valid_users))
    # for valid_user in valid_users:
    #     if valid_user.email== user_email:
    #         form = RecordFileForm()

    # print(UserInformation.objects.filter(
    #     email__multivalues=user_email).exists())
    # valid_users = list(users)

    # print(valid_user)
    # print(type(valid_user))
    # for valid_user in valid_users:
    #     print(valid_user)
    #     # if valid_user.email == user_email:
    #     #     return redirect('bmicalculate')

    # patient = UserInformation.objects.get(email=user_email)
    # print(patient)
    form = RecordFileForm()
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

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')

    records = RecordFile.objects.filter(email=user_email)
    print(records.datetimes)
    # print(records.__dict__.keys())
    context = {'records': records}
    return render(request, 'base/viewrecord.html', context)

# def menu(request):
#     return render(request, 'menu.html')


@login_required(login_url='loginuser')
def bmicalculate(request):

    user_email = request.user.email

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')
    resultinterface = False
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
        if bmi < 18.5:
            below = True
        if bmi >= 18.5 and bmi <= 25:
            good = True
        if bmi > 25 and bmi <= 30:
            above = True
        if bmi > 30:
            obsess = True

        resultinterface = True
        context = {'bmi': bmi, 'good': good, 'above': above, 'below': below, 'obsess': obsess, 'resultinterface': resultinterface,
                   }
        return render(request, 'base/bmicalculate.html', context)
        # return redirect('bmiresult', context)
    context = {}
    return render(request, 'base/bmicalculate.html', context)


@login_required(login_url='loginuser')
def bmiresult(request):

    context = {}
    return render(request, 'base/bmicalculate.html', context)


@login_required(login_url='loginuser')
def addhealthinfo(request):

    user_email = request.user.email

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')

    form = HealthInfoForm()
    # user_email = request.user.email
    healthinfos = HealthInfo.objects.filter(email=user_email)
    if request.method == 'POST':
        form = HealthInfoForm(request.POST)
        form.instance.email = user_email
        if form.is_valid():
            form.save()
            return redirect('addhealthinfo')

    context = {'form': form, 'healthinfos': healthinfos}
    return render(request, 'base/addhealthinfo.html', context)


@login_required(login_url='loginuser')
def dietrecord(request):

    user_email = request.user.email

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')

    form = DietRecordForm()

    if request.method == 'POST':
        form = DietRecordForm(request.POST)
        form.instance.email = user_email
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/dietrecord.html', context)


@login_required(login_url='loginuser')
def viewdietrecord(request):
    user_email = request.user.email

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')

    dietrecords = DietRecord.objects.filter(email=user_email)
    context = {'dietrecords': dietrecords}
    return render(request, 'base/viewdietrecord.html', context)


@login_required(login_url='loginuser')
def exerciserecord(request):
    user_email = request.user.email

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')

    form = ExerciseRecordForm()

    if request.method == 'POST':
        form = ExerciseRecordForm(request.POST)
        form.instance.email = user_email
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/exerciserecord.html', context)


@login_required(login_url='loginuser')
def viewexerciserecord(request):
    user_email = request.user.email

    valid_users = list(UserInformation.objects.all().values('email'))
    valid = False

    for valid_user in valid_users:
        if valid_user["email"] == user_email:
            valid = True

    if not valid:
        return redirect('userinfo')

    exerciserecords = ExerciseRecord.objects.filter(email=user_email)
    context = {'exerciserecords': exerciserecords}

    return render(request, 'base/viewexerciserecord.html', context)
