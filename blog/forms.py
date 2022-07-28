from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets
#from django.forms.models import _Labels
from django.utils.translation import gettext, gettext_lazy as _
from .models import post
#from blog import models

#from django.forms import fields
class SignupForm (UserCreationForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label=' Confirm Password (Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email','username':'UaerName'}

        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),

         'first_name':forms.TextInput(attrs={'class':'form-control'}),
         'email':forms.EmailInput(attrs={'class':'form-control'}),
         'password':forms.PasswordInput(attrs={'class':'form-control'}),

        }
class loginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("password"),strip=False, widget= forms.TextInput(attrs={'autocomplete': 'new-password','class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields = ['name','titel','dec']
        labels = {'Name':'name','titel':'Titel','dec':'descriptions'}
        widgets = {'titel':forms.TextInput(attrs={'class':'form-control'}),
         'dec':forms.Textarea(attrs={'class':'form-control'}),
         'name':forms.TextInput(attrs={'class':'form-control'}),
        }