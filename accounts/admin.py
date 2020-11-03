from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        'email', 'username', 'first_name', 'last_name', 'DOB', 'date_joined', 'last_login', 'is_staff', 'is_admin'
    )

    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
