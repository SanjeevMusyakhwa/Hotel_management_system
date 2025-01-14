from django.contrib import admin
from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'phone_number', 'username', 'email']
    list_display = ['full_name', 'username', 'email', 'phone_number', 'gender']

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__full_name', 'user__phone_number', 'user__username']
    list_display = [
        'get_full_name', 
        'get_username', 
        'get_email', 
        'get_phone_number', 
        'get_gender', 
        'verified'
    ]

    def get_full_name(self, obj):
        return obj.user.full_name
    get_full_name.admin_order_field = 'user__full_name'  # Allows ordering by full_name
    get_full_name.short_description = 'Full Name'

    def get_username(self, obj):
        return obj.user.username
    get_username.admin_order_field = 'user__username'
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'

    def get_phone_number(self, obj):
        return obj.user.phone_number
    get_phone_number.admin_order_field = 'user__phone_number'
    get_phone_number.short_description = 'Phone Number'

    def get_gender(self, obj):
        return obj.user.gender
    get_gender.admin_order_field = 'user__gender'
    get_gender.short_description = 'Gender'

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
