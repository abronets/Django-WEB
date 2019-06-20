from allauth.account.forms import SignupForm
from allauth.account.views import SignupView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView

from .forms import LoginForm


# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/'


class UserDetailView(DetailView):
    template_name = 'users/user_detail.html'
    model = get_user_model()


class UserRegister(SignupView):
    form_class = SignupForm
    redirect_field_name = "next"
    success_url = '/'
