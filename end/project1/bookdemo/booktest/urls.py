# author sqz
# date 2020/2/13 14:35
# file_name urls

from django.conf.urls import url
from . import views

# 2. 每一个路由文件中必须编写
urlpatterns =[
    url(r'^index/$',views.index),
    #使用正则分组可以向视图函数中传递参数
    #第一个参数就是路由  第二个参数就是视图函数
    #第一个参数中如果有正则分组 小括号 则正则分组匹配的内容会作为实参传递给视图函数
    url(r'detail/(\d+)/',views.detail),
    url(r'^about/$',views.about),

]