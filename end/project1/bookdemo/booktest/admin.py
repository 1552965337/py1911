from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.

# django 自带的后台管理操作需要再此实现
# 注册自己需要管理的模型  Book  Hero

from .models import Book,Hero,User

class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    extra = 4

class HeroAdmin(ModelAdmin):
    list_display = ('name','gender','content','book')

admin.site.register(Hero,HeroAdmin)

class BookAdmin(ModelAdmin):
    """
    定义模型管理类
    通过该类可以修改后台页面
    """
    #更改后端显示列
    list_display = ('title','price','pub_date')
    #每页显示2个
    # list_per_page = 2
    #定义后端搜索字段
    search_fields = ('title','price')
    #指定过滤字段
    list_filter = ('title','price')
    #关联
    inlines = [HeroInline]

admin.site.register(Book,BookAdmin)

admin.site.register(User)