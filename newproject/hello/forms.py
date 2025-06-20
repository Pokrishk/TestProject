from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserAccount

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Подтверждение пароля')

    class Meta:
        model = UserAccount
        fields = ['firstname', 'lastname', 'middlename', 'email', 'password']
        labels = {
            'firstname': 'Имя',
            'lastname': 'Фамилия',
            'middlename': 'Отчество',
            'email': 'Электронная почта',
            'password': 'Пароль',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Пароли не совпадают')
            
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Электронная почта')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
