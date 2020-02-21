# author sqz
# date 2020/2/20 9:26
# file_name urls
from django.conf.urls import url
from . import views
from .feed import ArticleFeed

app_name='blogapp'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^favicon.ico/$',views.favicon),
    url(r'^rss/$',ArticleFeed(),name="rss")
]