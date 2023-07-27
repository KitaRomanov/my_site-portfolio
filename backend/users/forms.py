from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User
from users.tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ваше имя'}))
    planet = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'с какой вы планеты'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваш никнейм'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'type': 'text', 'placeholder': 'Введите вашу почту'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'planet', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        send_email_verification.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': ''}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
