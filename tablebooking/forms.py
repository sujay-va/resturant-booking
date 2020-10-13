from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class Resturantform(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class Booktableform(ModelForm):
    class Meta:
        model = BookTable
        fields = '__all__'


class Orderdishform(ModelForm):
    class Meta:
        model = OrdersDish
        fields = '__all__'
