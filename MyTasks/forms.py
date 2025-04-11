from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя..'
    }))

    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль..'
    }))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя..'
    }))

    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия..'
    }))

    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта..'
    }))

    username = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя..'
    }))

    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль..'
    }))

    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль..'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'title', 'description', 'due_date'}
        widgets = {
            'title': forms.TextInput(attrs={

            })
        }

class TaskFormAddContent(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),

            'due_date': forms.DateInput(attrs={
                'class': 'form-control'
            })
        }