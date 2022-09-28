import email
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile




class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2']
    


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    image = forms.ImageField()
    class   Meta:
        model = Profile
        fields = ['image']