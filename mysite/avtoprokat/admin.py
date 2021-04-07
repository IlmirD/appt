from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Car

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CarAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'created', 'added')
    search_fields = ('name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, AccountAdmin)
admin.site.register(Car, CarAdmin)