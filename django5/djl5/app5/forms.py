from django import forms
from app5.models import userpro
from django.contrib.auth.models import User

class userproform(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    #portfolio = forms.URLField(required=False)
    #picture  forms.ImageField(required=False)

    class Meta():
        model = User
        fields = ('username','email','password')

class userproinfo(forms.ModelForm):

    class Meta():
        model = userpro
        fields =('portfolio','profile_pics')
