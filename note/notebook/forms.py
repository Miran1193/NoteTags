from django import forms
from .models import Note, Tag
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your E-Mail'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=50, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CreateNoteForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter title note'}))
    text = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter text note'}))
    tags = forms.ModelChoiceField(queryset=Tag.objects.all(), required=True,
                                  widget=forms.Select(attrs={'placeholder': 'Select a tag'}))

    class Meta:
        model = Note
        fields = ['title', 'text', 'tags']
