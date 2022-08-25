from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import User, Tasks

class UserModelAdmin(UserAdmin):
    list_display = ('username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('username', 'date_joined')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserModelAdmin)
admin.site.register(Tasks)
