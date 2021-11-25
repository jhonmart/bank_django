from django.contrib import admin
from users.models import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'sex', 'mail')
    list_filter = ('id', 'name', 'birthday', 'sex', 'mail')
    search_fields = ('id', 'name', 'birthday', 'sex', 'mail')
