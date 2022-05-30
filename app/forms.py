from dataclasses import field
from urllib import request
from django import forms
from django.forms import ModelForm, Select, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class PostCommentForm(ModelForm):
    class Meta:
        model = PostComment
        fields = ['username', 'like', 'comment']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'}),

            'like': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Like or dislike'}),

            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Comment'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'firstname' : forms.TextInput(
                attrs={'class' : 'form-control'}
            ),
            'lastname': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'subject': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
               'message': forms.Textarea(
                attrs={'class': 'form-control'}
            )
        }