from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    fieldsets  = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields":("email",)}),

    )

    add_fieldsets = (
        (None, {"fields": ("username","email", "password1", "password2"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)