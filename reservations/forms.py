from django import forms
from django.forms import ModelForm
from .models import Users


# Create a new user
class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ('Name', 'Email', 'Password')

        widgets = {
            'Name':
            forms.TextInput(attrs={'class': 'form-control',
                                   'placeholder': 'Enter your name'}),
            'Email':
            forms.EmailInput(attrs={'class': 'form-control',
                                    'placeholder': 'Enter your email'}),
            'Password':
            forms.PasswordInput(attrs={'class': 'form-control',
                                       'placeholder': 'Enter your password'}),
            }
