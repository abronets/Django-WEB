from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from .forms import AddUserForm
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'is_staff')
    add_form = UserCreationForm
    form = AddUserForm
