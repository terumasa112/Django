from django.contrib import admin

# Register your models here.

from.models import CustomUser

#管理画面にユーザ登録アプリを登録する
admin.site.register(CustomUser)