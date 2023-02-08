from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import forms as auth_forms
from account.choices import GENDER

user_model = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # todo check if I need this form
    class Meta:
        model = user_model
        fields = ('email','password',)


class CustomUserChangeForm(UserChangeForm):
    # todo
    class Meta:
        model = user_model
        fields = ('email','password')


class LoginForm(auth_forms.AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user_model
        fields = ('password',)
    


class UserEditForm(auth_forms.UserChangeForm):
    password = None
    class Meta:
        model = user_model
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name',
            'phone_number', 'gender', 'photo')

class RegisterForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER)
    
    class Meta:
        model = user_model
        fields = ('first_name', 'last_name','middle_name','email', 'gender', 'phone_number','username', 'password1', 'password2' , 'photo')

class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
