from django.contrib import admin

from users.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'telegram', 'avatar')