from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.models import User

admin.site.site_header = 'Lead Manager'
admin.site.site_title = "Lead Manager"
admin.site.index_title = "Welcome"

class UserAdmin(BaseUserAdmin):
    
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'last_login')
    list_filter = ('is_staff', )
    fieldsets = (
        ('Login Details', {'fields': ('email', 'password', 'username',)}),
        ('Personal Details', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes' : ('wide',),
                'fields' : (
                    'email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name', 'date_joined')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)