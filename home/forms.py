

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput, Textarea, TextInput
 

from . models import CustomUser




class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "name":"password1",'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "name":"password2",'placeholder': 'Confirm Password'}))

    class Meta:
        
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'address',
        ]
                
        widgets = {
            'username' : TextInput(attrs={"class":"form-control", "name":"username", "placeholder":"Username"}),
            'email' : TextInput(attrs={"class":"form-control", "name":"email", "placeholder":"Enter Email"}),
            'address' : TextInput(attrs={"class":"form-control", "name":"address", "placeholder":"Enter Address"})      

        }   
    
