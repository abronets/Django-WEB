from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from .models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control'
            }
        ),
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
    )


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser',)




