from django.contrib import admin

from .models import Author, AuthorDetail, Course, Tag

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    '''映射类对应的后台管理类
    '''

    list_display = ['id', 'name', 'gender']


admin.site.register(Author, AuthorAdmin)

for model in (AuthorDetail, Course, Tag):
    admin.site.register(model)

