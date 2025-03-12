from django import forms
from django.contrib.auth.models import User
from registerapp.models import Userprofile

from django_recaptcha.fields import ReCaptchaField

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password','email']
class UserprofileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=['address','street','city','zipcode','img']
    captcha=ReCaptchaField() 

class UpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
class UserprofileUpdateForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=['address','street','city','zipcode','img']

