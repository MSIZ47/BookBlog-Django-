from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm  # for adding new users
    form = CustomUserChangeForm  # for regular situation or editing
    model = CustomUser
    fieldsets = BaseUserAdmin.fieldsets + (     # it is for form attribute(showing on admin panel)
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (   # it is for add_form attribute(creating)
        (None, {'fields': ('first_name', 'last_name', 'age',)}),
    )


admin.site.register(CustomUser, UserAdmin)
