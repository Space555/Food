from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.CharField(required=True, label='', widget=forms.EmailInput(attrs={'placeholder': 'Email *',
                                                                                    'class': 'register-input'}))
    password1 = forms.CharField(required=True, label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль *',
                                                                  'class': 'register-input pass1'}))
    password2 = forms.CharField(required=True, label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль *',
                                                                  'class': 'register-input pass2'}))

    first_name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Имя *',
                                                                                        'class': 'register-input'}))
    last_name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Фамилия *',
                                                                                       'class': 'register-input'}))
    # avatar = forms.ImageField(required=True, label='', widget=forms.FileInput(attrs={'class': 'register__image'}))
    city = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'register__city',
                                                                                  'placeholder': 'Город'}))

    class Meta:
        model = User
        fields = 'email', 'password1', 'password2', 'first_name', 'last_name'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user