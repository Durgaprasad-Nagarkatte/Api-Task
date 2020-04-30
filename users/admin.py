from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ('username', 'password1', 'password2', 'first_name', "last_name", "timezone", 'user_id'),
                },
            ),
        )

admin.site.register(CustomUser, CustomUserAdmin)