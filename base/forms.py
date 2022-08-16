from dataclasses import fields
from statistics import mode
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['username', 'email', 'password1', 'password2']
        fields = ['email', 'password1', 'password2']


class UserInformationForm(ModelForm):
    class Meta:
        model = UserInformation
        fields = ['name', 'age', 'gender', 'weight']
