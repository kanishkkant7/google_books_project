from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AuthForm(AuthenticationForm):
    username=forms.CharField(max_length=10,widget=forms.TextInput(
        attrs={
        'class': 'form-control',
         'placeholder': 'Username',
         "aria-label":"Username",
         "aria-describedby":"addon-wrapping"
        }))
    password = forms.CharField(max_length=12,widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Password',
            "aria-label":"Username", 
            "aria-describedby":"addon-wrapping"
        }))
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'aria-label': 'First Name',
            'aria-describedby': 'addon-wrapping'
        })
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            'aria-label': 'Last Name',
            'aria-describedby': 'addon-wrapping'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'aria-label': 'Email',
            'aria-describedby': 'addon-wrapping'
        })
    )
    username = forms.CharField(max_length=10,widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'aria-label': 'Username',
            'aria-describedby': 'addon-wrapping'
        }
    ))
    password1 = forms.CharField(max_length=12,widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'aria-label': 'Password',
            'aria-describedby': 'addon-wrapping'
        }
    ))
    password2 = forms.CharField(max_length=12,widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'aria-label': 'Confirm Password',
            'aria-describedby': 'addon-wrapping'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user