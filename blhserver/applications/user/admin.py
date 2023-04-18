from django.contrib import admin
from applications.user.models import User, Address, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uid', 'username', 'mobile', 'create_time')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_time')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'user', 'address', 'goods', 'status')
