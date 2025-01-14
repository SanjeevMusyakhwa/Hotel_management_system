from django.contrib import admin
from .models import User, Profile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
  search_fields = ['full_name, phone_number', 'username', 'email']
  list_display=['full_name', 'username', 'email', 'phone_number', 'gender']

class ProfileAdmin(admin.ModelAdmin):
  search_fields = ['full_name', 'phone_number', 'user__username' ]
  list_display =['full_name', 'username', 'email', 'phone_number', 'gender', 'verified']
admin.site.register(User, UserAdmin)