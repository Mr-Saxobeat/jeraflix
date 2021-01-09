from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomAccount, Profile

class CustomAccountAdmin(UserAdmin):
    model = CustomAccount
    list_display = ['username', 'email', 'is_staff']

admin.site.register(CustomAccount, CustomAccountAdmin)
admin.site.register(Profile)
