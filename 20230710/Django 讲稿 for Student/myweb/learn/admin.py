from django.contrib import admin
# Register your models here.
from .models import Author, AuthorDetail, Course, Tag

# 配置修改Author的其他字段
'''
    映射类对应的后台管理类
'''
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']

admin.site.register(Author, AuthorAdmin)

for model in (AuthorDetail, Course, Tag):
    admin.site.register(model)

