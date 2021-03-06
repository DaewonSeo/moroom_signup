from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(ModelForm):

    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  ]
        labels = {
            'username': '아이디'
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['contact']
        labels = {
            'contact': '연락처'
        }

class LoginForm(ModelForm):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': '아아디'
        }


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
