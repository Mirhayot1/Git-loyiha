from django import forms
# from django.contrib.auth.models import User
# from django.forms.utils import ErrorList
# from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)