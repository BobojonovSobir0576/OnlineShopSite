from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import forms as auth_forms
from account.choices import GENDER
from account.models import *

user_model = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # todo check if I need this form
    class Meta:
        model = user_model
        fields = ('first_name', 'last_name','email', 'gender', 'phone_number','username', 'password1', 'password2' , 'photo')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.set_password(self.cleaned_data.get('password'))
        user.username = self.cleaned_data.get('username')
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    # todo
    class Meta:
        model = user_model
        fields = ('email','password')


class LoginForms(auth_forms.AuthenticationForm):
    pass
    


class UserEditForm(auth_forms.UserChangeForm):
    password = None
    class Meta:
        model = user_model
        fields = ('username', 'email', 'last_name', 'first_name',
            'phone_number', 'gender', 'photo')

class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
